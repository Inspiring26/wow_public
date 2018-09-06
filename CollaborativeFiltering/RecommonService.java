package com.sunsheen.ywnw.service;

import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.VoidFunction;
import org.apache.spark.sql.DataFrame;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SQLContext;

import com.sunsheen.ywnw.utils.DBUtil;
import com.sunsheen.ywnw.utils.HdfsUtil;

public class RecommonService {

	public static void main(String[] args) throws IOException{
		System.setProperty("hadoop.home.dir", "D:\\JAVA\\hadoop");
		SparkConf conf = new SparkConf()
				.setAppName("Test")
				.setMaster("spark://10.158.90.57:7077");
		JavaSparkContext sc = new JavaSparkContext(conf);
		//一些匿名内部类在集群上无法调用，因此需要在本地打包，并通过addJar方式上传
		//使用maven工具打包：maven install... 填写goals为package
		sc.addJar("file:///D:/JAVA/workspace/ywnw/target/ywnw-0.0.1-SNAPSHOT.jar");
		//读取数据库数据转换为
		SQLContext sqlContext = new SQLContext(sc);
		DBUtil.register(sqlContext,"weblog");
		DataFrame resultDF =sqlContext.sql("select text,userip,url from weblog"); 
        List<Row> listRow = resultDF.javaRDD().collect();//.collect();
        
        //组织数据库数据--开始
        int udfN = 0;
        for(Row row : listRow){
        	int pos = row.get(2).toString().indexOf("undefined");
        	if (pos != -1) {
        		udfN++;
        	}
        }
        String[][] inputArray = new String[listRow.size()-udfN][2];
        String[] tittleLinkArray0 = new String[listRow.size()-udfN];
        String[] tittleLinkArray1 = new String[listRow.size()-udfN];
        int n = 0;  
        for(Row row : listRow){
        	int pos = row.get(2).toString().indexOf("undefined");
        	if (pos != -1) {
        		continue;
        	}
        	inputArray[n][0] = row.get(0).toString();
        	inputArray[n][1] = row.get(1).toString();
        	tittleLinkArray0[n] = row.get(0).toString();
        	tittleLinkArray1[n++] = row.get(2).toString();    
        }
        //组织数据库数据--结束
        


        //新用户推荐 返回字符串组包含 标题列和链接列
        String[][] rmd4NewUsrList = recommend4NewUsr(inputArray,tittleLinkArray0,tittleLinkArray1);
        printAllOfArr(rmd4NewUsrList);

        // 全部用户推荐
        String[][] resulList = recommend4AllUsr(inputArray,rmd4NewUsrList, tittleLinkArray0, tittleLinkArray1);
        printAllOfArr(resulList);
        
       
        
       
	}




	
	//所有已存在用户做推荐 返回字符串组包含 ip列 标题列 链接列
	public static String[][] recommend4AllUsr(String[][] inArr,String[][] rmdArr, String[] tittleLinkArray0, String[] tittleLinkArray1) throws IOException{
		//IP列表
        String[] users4result = createUserArr(inArr);
        //创建结果矩阵
        String[][] maybeResultList = new String[5*users4result.length][3];


        int splN=0;
        for(int i=0;i<users4result.length;i++) {
        	//获取i用户的5条推荐
        	String[][] strArr = controller(inArr,users4result[i]);
        	//对这个数组进行处理，处理的结果是包含符合条件的标题列和符合条件的链接列
        	//解决办法是 建立一个十行的数组，把controller返回的推荐数组和给新用户推荐的数组组合在一起，取前5个
        	String[] tenLenArr = new String[10];
        	int tenN=0;
        	// 把符合条件的controller返回的加进来
        	for (int j=0;j<strArr.length ;j++ ) {
        		if (strArr[j][0]==null) {
        			continue;
        		}
        		if (strArr[j][0].equals("null")) {
        			continue;
        		}
        		tenLenArr[tenN++]=strArr[j][0];
        	}
        	// 把符合条件的 对新用户的推荐加进来
        	for (int j=0; j<rmdArr.length; j++) {
        		if (rmdArr[j][0]==null) {
        			continue;
        		}
        		int pos= indexOfArr(tenLenArr, rmdArr[j][0]);
        		if (pos == -1) {
        			tenLenArr[tenN++]=rmdArr[j][0];
        		}

        	}
        	// 到这里获取了一个不重复的大于5个的controller返回优先的长为10的列表

        	// 把这5个写到maybeResultList里，并同时写上链接
        	for (int j=0; j<5 ;j++ ) {
        		maybeResultList[splN][0] = users4result[i];
        		maybeResultList[splN][1] = tenLenArr[j];

        		int pos= indexOfArr(tittleLinkArray0, tenLenArr[j]);
        		maybeResultList[splN++][2] = tittleLinkArray1[pos];
        	}	
        }
        
        return maybeResultList;
	}

	

	//为新用户推荐
	//传入 数据库的标题列和ip列  数据库的标题列 数据库的链接列
	//返回 标题列和链接列 的二维字符串组
	public static String[][] recommend4NewUsr(String[][] inArr,String[] tittleList,String[] linkList){
		//获取不重复的标题列
		String[] tittles4result = createItemArr(inArr);
        //String[] forNewUser = new String[tittles4result.length];
		//为标题列做计数
        int[] forNewUserAmount = new int[tittles4result.length];
        //初始化计数列
        for(int i=0;i<tittles4result.length;i++) {forNewUserAmount[i]=0;}

        //计数部分--开始
        for(int i=0;i<inArr.length;i++) {
        	String tempStr = inArr[i][0];
        	int pos= indexOfArr(tittles4result, tempStr);
        	forNewUserAmount[pos]++;
        	
        }
        //计数部分--结束

        //给新用户推荐5个 但是获取十个，因为要过滤一些
        //这里获取的是索引
        int[] max5Index4NewUser = max_n_indexOfArr(forNewUserAmount, 15);
        // 测试一下
        // for (int i=0;i< max5Index4NewUser.length; i++) {
        // 	System.out.println(forNewUserAmount[max5Index4NewUser[i]]);
        // }
		// 测试结果
		// 943
		// 908
		// 618
		// 534
		// 349
		// 306
		// 228
		// 223
		// 219
		// 218
		// 214
		// 197
		// 187
		// 165
		// 164
        //创建返回字符串组，包含标题列和链接列
        String[][] tittleLink4New = new String[5][2];

        //生成返回数组--开始
        int extNum = 0;
        for(int i=0;i<15;i++) {
        	String[] stopWords = new String[]{"首页","","null","天气业务","观测业务","服务业务","气候业务"};
        	
        	int pos0 = indexOfArr(stopWords, tittles4result[max5Index4NewUser[i]]);
        	//System.out.println(pos0); 通过这里可以看见前6个都是在停用词里的
        	if (pos0 != -1)continue;
        	tittleLink4New[extNum][0]= tittles4result[max5Index4NewUser[i]];//tittle
        	
        	int pos= indexOfArr(tittleList, tittleLink4New[extNum][0]);
        	tittleLink4New[extNum++][1]= linkList[pos];//link
        	if(extNum==5)break;
        }
        //生产返回数组--结束
        return tittleLink4New;

	}
	
	public static int[] max_n_indexOfArr(int[] arr, int n){
		// Arrays类之只是提供了默认的升序排列，没有提供相应的降序排列方法
		// int num = 5;
		int[] sortedArr = new int[arr.length];
		sortedArr = (int[])arr.clone();
		Arrays.sort(sortedArr);
		
		int[] arrCopy = new int[arr.length];
		arrCopy = (int[])arr.clone();


		int[] returnArray = new int[n];
		for (int i=sortedArr.length-1;i>=sortedArr.length-n ;i-- ) {
			int pos = indexOfArr(arrCopy,sortedArr[i]);
			returnArray[sortedArr.length-i-1]=pos;
		}

		

		return returnArray;
		// 测试数据
		// double[]{1.1, 2.2, 0.3, 5.6, 8.9, 3.3, 1.6};
		// 结果 4 3 5 1 6
	}
	public static int indexOfArr(int[] inputArray,int value){
		for (int i=0;i<inputArray.length ;i++ ) {
			if(inputArray[i]==(value)){
				return i;

			}
		}
		return -1;
	}
	// 控制器
		public static String[][] controller(String[][] inputArray,String ipname)throws IOException{
			// 从xls里获取两列数据
			// 创建不重复的商品的数组
			String[] items = createItemArr(inputArray);
			// 创建不重复的用户的数组
			String[] users = createUserArr(inputArray);
			// 获取用户在用户数组的索引
			int queryUserId = indexOfArr(users,ipname);
			// 创建用户对商品喜爱度矩阵
			int[][] dfArray = array2dfArray(inputArray,items,users);
			// 创建用户相似度矩阵
			double[][] similarity = cosine_similarity_matrix(dfArray);
			// 和此用户最相似的前n个用户的索引矩阵
			double[] one2others = similarity[queryUserId];
			// 选择最相似的前一半
			int[] posArr = max_n_indexOfArr(one2others, (int)(similarity[0].length));

			// 权重结果矩阵
			double[] weightMatrix = likeArray(dfArray, similarity, posArr,queryUserId);
			// 获取数组中最大的前n个shangpin的索引
			int[] weightIndex = max_n_indexOfArr(weightMatrix, 20);

			// 结果矩阵 提供9个，筛选后留5个
			// 把结果矩阵变为二维矩阵，添加权重信息
			String[][] resultMatrix = new String[5][2];
			// resultMatrix单独计数
			int im_n = 0;
			// 停用词数组
			String[] stopWords = new String[]{"首页","","null","天气业务","观测业务","服务业务","气候业务"};
			// System.out.println("begin......");
			for (int i=0;i<weightIndex.length ;i++ ) {
				// 获取词在停用词中的位置，如果没有，则返回-1
				int pos = indexOfArr(stopWords, items[weightIndex[i]]);
				// System.out.println(pos);
				if (pos==-1) {
					resultMatrix[im_n][0] = items[weightIndex[i]];
					resultMatrix[im_n][1] = String.valueOf(weightMatrix[weightIndex[i]]);

					im_n++;
				}
				if (im_n==5)break;
				
			}
			return resultMatrix;
		}
		public static String[] linkArray(String[][] resultStr, String[][] linkStr){
			String[] linkStr0 = new String[resultStr.length];
			String[] returnLink = new String[resultStr.length];
			for (int i=0; i<resultStr.length; i++) {
				linkStr0[i] = resultStr[i][0];
			}
			for (int i=0;i<resultStr.length ; i++) {
				String tempStr = resultStr[i][0];
				int pos = indexOfArr(linkStr0, tempStr);
				returnLink[i]=linkStr[pos][1];
			}
			return returnLink;
			
		}

		// 创建商品数组
		public static String[] createItemArr(String[][] inputArray){
			Set set0=new HashSet();
			for (int i=0;i<inputArray.length ;i++ ) {
				set0.add(inputArray[i][0]);
			}
			int n_items = set0.size();
			String[] items = new String[n_items];
			int num=0;
			for( Iterator   it = set0.iterator();  it.hasNext();){
				items[num] = it.next().toString();
				num+=1;
			}
			return items;
		}
		// 创建用户数组
		public static String[] createUserArr(String[][] inputArray){
			Set set1=new HashSet();
			for (int i=0;i<inputArray.length ;i++ ) {
				set1.add(inputArray[i][1]);
			}
			int n_users = set1.size();
			String[] users = new String[n_users];
			int num=0;
			for( Iterator   it = set1.iterator();  it.hasNext();){
				users[num] = it.next().toString();
				num+=1;
			}
			return users;
		}
		public static int indexOfArr(String[] inputArray,String value){
			for (int i=0;i<inputArray.length ;i++ ) {
				if (inputArray[i]==null) {
					return -1;
				}
				if(inputArray[i].equals(value)){
					return i;
				}
			}
			return -1;
		}
		public static int indexOfArr(double[] inputArray,double value){
			for (int i=0;i<inputArray.length ;i++ ) {
				if(inputArray[i]==(value)){
					return i;
				}
			}
			return -1;
		}
		// 建立一个类事java中df格式的二维矩阵
		public static int[][] array2dfArray(String[][] inputArray,String[] items,String[] users){
			// 创建df格式数组
			int[][] returnArray = new int[users.length][items.length];
			// 创建整型数组，默认值是0
			// System.out.println(returnArray[1][1]);//验证
			// System.out.println(inputArray[0].length);//验证 之所以这么写是为了条理更清晰
			for (int i =0;i<inputArray.length ;i++ ) {
				// 查找在用户中的索引
				int x = indexOfArr(users,inputArray[i][1]);
				// 查找在商品中的索引
				int y = indexOfArr(items,inputArray[i][0]);
				returnArray[x][y] += 1;
			}
			return returnArray;
		}
		// 计算二维矩阵的行之间的余弦相似度
		public static double[][] cosine_similarity_matrix(int[][] arr){
			double[][] returnArray = new double[arr.length][arr.length];
			for (int i=0;i<arr.length ;i++ ) {
				for (int j=1;j<arr.length ;j++ ) {
					returnArray[i][j]=returnArray[j][i]=cosine_similarity(arr[i],arr[j]);
				}
			}
			return returnArray;
			// 要进行测试
			// int[][] testArray = new int[][]{{0,0},{0,1},{1,0},{1,1},};
		}
		// 计算两个向量的余弦相似度
		public static double cosine_similarity(int[] arr0,int[] arr1){
			if (arr0.length!=arr1.length) {
				System.out.println("传入的两个向量长度不相同");
			}
			// 分子numerator
			double numerator = 0.0d;
			// 分母denominator
			double denominator0 = 0.0d;
			double denominator1 = 0.0d;
			double denominatorTotal = 0.0d;
			for (int i=0;i<arr0.length ;i++ ) {
				numerator += (double)(arr0[i])*(double)(arr1[i]);
				denominator0 += (double)(arr0[i])*(double)(arr0[i]);
				denominator1 += (double)(arr1[i])*(double)(arr1[i]);
			}
			denominatorTotal = Math.sqrt(denominator0)*Math.sqrt(denominator1);
			// System.out.println(numerator);
			// System.out.println(denominatorTotal);
			if ((double)(denominatorTotal)==(double)(0)) {
				return (double)(0);//所以结果为0的，要么是垂直，使分子为0了，要么是有0向量，分母为0了
			}
			// 通过{0,0},{0,0}测试了
			return (numerator/denominatorTotal);
		}
		// 获取数组中最大的前n个的索引
		public static int[] max_n_indexOfArr(double[] arr, int n){
			// Arrays类之只是提供了默认的升序排列，没有提供相应的降序排列方法
			// int num = 5;
			double[] sortedArr = new double[arr.length];
			sortedArr = (double[])arr.clone();
			Arrays.sort(sortedArr);
			double[] arrCopy = new double[arr.length];
			arrCopy = (double[])arr.clone();
			int[] returnArray = new int[n];
			for (int i=sortedArr.length-1;i>=sortedArr.length-n ;i-- ) {
				int pos = indexOfArr(arrCopy,sortedArr[i]);
				returnArray[sortedArr.length-i-1]=pos;
			}
			return returnArray;
			// 测试数据
			// double[]{1.1, 2.2, 0.3, 5.6, 8.9, 3.3, 1.6};
			// 结果 4 3 5 1 6
		}
		// n个用户m个商品，每个用户对每个商品的like程度组成一个like数组
		// 传入 用户-商品矩阵（用户对商品喜爱度矩阵） 用户相似度矩阵 最相似前n个用户索引矩阵  要查询的用户的id
		public static double[] likeArray(int[][] dfArray, double[][] similarity, int[] posArr,int queryUserId){
			double[] likeArr = new double[dfArray[0].length];
			for (int i = 0;i<posArr.length ;i++ ) {
				// 用户编号
				int uid = posArr[i];
				// 此用户对各个商品的like程度
				for (int j=0;j<dfArray[0].length ;j++ ) {
					likeArr[j] += similarity[queryUserId][uid] * dfArray[uid][j];
				}
			}
			return likeArr;
		}
		// 打印数组，以供查看
		public static void printAllOfArr(String[] arr){
			for (int i=0;i<arr.length ;i++ ) {
				System.out.println(arr[i]);
			}
		}
		public static void printAllOfArr(int[] arr){
			for (int i=0;i<arr.length ;i++ ) {
				System.out.println(arr[i]);
			}
		}
		public static void printAllOfArr(int[][] arr){
			for (int i=0;i<arr.length ;i++ ) {
				for (int j=0;j<arr[0].length ;j++ ) {
					System.out.print(arr[i][j]+"\t");
				}
				System.out.println("");
			}
		}
		public static void printAllOfArr(String[][] arr){
			for (int i=0;i<arr.length ;i++ ) {
				for (int j=0;j<arr[0].length ;j++ ) {
					System.out.print(arr[i][j]+"\t");
				}
				System.out.println("");
			}
		}
		public static void printAllOfArr(double[][] arr){
			for (int i=0;i<arr.length ;i++ ) {
				for (int j=0;j<arr[0].length ;j++ ) {
					System.out.print(arr[i][j]+"\t");
				}
				System.out.println("");
				
			}
		}
		// 打印数组块结束
}
