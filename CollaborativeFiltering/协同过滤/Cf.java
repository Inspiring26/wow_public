import java.io.FileInputStream;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import java.io.IOException;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFCell;
import java.util.*;
// import java.util.Iterator;




public class Cf{
	public static String[][] xls2Array(String filename)throws IOException{
        FileInputStream inputStream=new FileInputStream(filename);
		//将输入流转换为workbook
		HSSFWorkbook workbook=new HSSFWorkbook(inputStream);
		//获取工作表
		HSSFSheet sheet=workbook.getSheetAt(0);
		// 获取行数 因为getLastRowNum()函数的因素要多加一列
		int rowNum=sheet.getLastRowNum() +1;
		// // 打印行数
		// System.out.println(rowNum);
		// 创建二维数组
		String[][] returnArray = new String[rowNum][2];
		String str0="",str1="";
		for (int i=0;i<rowNum ;i++ ) {
			HSSFRow row=sheet.getRow(i);
			HSSFCell cell0=row.getCell(2);
			if(cell0==null){
				str0 = "";
			}
			else{
				str0 = cell0.getStringCellValue();
			}

			HSSFCell cell1=row.getCell(5);
			if(cell1==null){
				str1 = "";
			}
			else{
				str1 = cell1.getStringCellValue();
			}
			returnArray[i][0]=str0;
			returnArray[i][1]=str1;
		}
		
		// System.out.println(rowNum);
		// System.out.println(returnArray[0][0]);
		// System.out.println(returnArray[rowNum-1][1]);
		// 结果是：
		// text
		// 10.158.46.76
		// 换成第六列发现运行结果有问题，并不是最后一行，而是倒数第二行，是getLastRowNum();函数的原因
		// 所以要多加一列
		// 结果是：
		// 	14701
		// 	text
		// 	9/27/2017 10:23:25
		// 通过验证
		// System.out.println(returnArray.length);

		return returnArray;
	}

	// 获取xls某一列信息
	public static String[] xls2Array(String filename, int n)throws IOException{
        FileInputStream inputStream=new FileInputStream(filename);
		//将输入流转换为workbook
		HSSFWorkbook workbook=new HSSFWorkbook(inputStream);
		//获取工作表
		HSSFSheet sheet=workbook.getSheetAt(0);
		// 获取行数 因为getLastRowNum()函数的因素要多加一列
		int rowNum=sheet.getLastRowNum() +1;
		// // 打印行数
		// System.out.println(rowNum);
		// 创建二维数组
		String[] returnArray = new String[rowNum];
		String str0="",str1="";
		for (int i=0;i<rowNum ;i++ ) {
			HSSFRow row=sheet.getRow(i);
			HSSFCell cell0=row.getCell(n);
			if(cell0==null){
				str0 = "";
			}
			else{
				str0 = cell0.getStringCellValue();
			}

			
			returnArray[i]=str0;
			
		}
		
		// System.out.println(rowNum);
		// System.out.println(returnArray[0][0]);
		// System.out.println(returnArray[rowNum-1][1]);
		// 结果是：
		// text
		// 10.158.46.76
		// 换成第六列发现运行结果有问题，并不是最后一行，而是倒数第二行，是getLastRowNum();函数的原因
		// 所以要多加一列
		// 结果是：
		// 	14701
		// 	text
		// 	9/27/2017 10:23:25
		// 通过验证
		// System.out.println(returnArray.length);

		return returnArray;
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

	public static int indexOfArr(String[] inputArray,String value){
		for (int i=0;i<inputArray.length ;i++ ) {
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
	// 控制器
	public static String[][] controller(String filename,String ipname)throws IOException{
		// 从xls里获取两列数据
		String[][] inputArray = xls2Array("log.xls");
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
		int[] weightIndex = max_n_indexOfArr(weightMatrix, 9);

		// 结果矩阵 提供9个，筛选后留5个
		// 把结果矩阵变为二维矩阵，添加权重信息
		String[][] resultMatrix = new String[5][2];
		// resultMatrix单独计数
		int im_n = 0;
		// 停用词数组
		String[] stopWords = new String[]{"首页",""};
		for (int i=0;i<weightIndex.length ;i++ ) {
			// 获取词在停用词中的位置，如果没有，则返回-1
			int pos = indexOfArr(stopWords, items[weightIndex[i]]);
			if (pos==-1) {
				resultMatrix[im_n][0] = items[weightIndex[i]];
				resultMatrix[im_n][1] = String.valueOf(weightMatrix[weightIndex[i]]);

				im_n++;
			}
			if (im_n==5)break;
			
		}

		return resultMatrix;



	}


}