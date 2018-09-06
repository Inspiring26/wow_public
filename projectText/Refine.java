import java.util.Date;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.ansj.splitWord.analysis.NlpAnalysis;
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

import org.ansj.splitWord.analysis.NlpAnalysis;


public class Refine{
	public static String[] fromExcel2TextArray(int num) throws IOException {
		String filepath = "测试数据1.xls";
        //读取excel文件 和读取其他文件没什么区别
        FileInputStream inputStream=new FileInputStream(filepath);
        //将输入流转换为workbook
        @SuppressWarnings("resource")
		HSSFWorkbook workbook=new HSSFWorkbook(inputStream);
        //获取工作表
        HSSFSheet sheet=workbook.getSheetAt(0);
        int rowNum;
        if(num==0) {
        		rowNum=sheet.getLastRowNum();
        }
        else {
        		rowNum = num;
        }
//        int rowNum=sheet.getLastRowNum();
//        int rowNum = 1001;
        String[] sheetData = new String[rowNum];
        for (int i=1;i<rowNum ; i++) {
                HSSFRow row=sheet.getRow(i);
                HSSFCell cell=row.getCell(1);
                String str = cell.getStringCellValue();
                sheetData[i] = str;
        }
		return sheetData;
	}
	
	public static String[] fromExcel2LabelArray(int num) throws IOException {
		String filepath = "测试数据1.xls";
        //读取excel文件 和读取其他文件没什么区别
        FileInputStream inputStream=new FileInputStream(filepath);
        //将输入流转换为workbook
        @SuppressWarnings("resource")
		HSSFWorkbook workbook=new HSSFWorkbook(inputStream);
        //获取工作表
        HSSFSheet sheet=workbook.getSheetAt(0);
        int rowNum;
        if(num==0) {
        		rowNum=sheet.getLastRowNum();
        }
        else {
        		rowNum = num;
        }
//        int rowNum=sheet.getLastRowNum();
//        int rowNum = 1001;
        String[] LabelData = new String[rowNum];
        for (int i=1;i<rowNum ; i++) {
                HSSFRow row=sheet.getRow(i);
                HSSFCell cell=row.getCell(2);
                String str = cell.getStringCellValue();
                LabelData[i] = str;
        }
		return LabelData;
	}
	
	public static String[] fromExcel2LittleLabelArray(int num) throws IOException {
		String filepath = "测试数据1.xls";
        //读取excel文件 和读取其他文件没什么区别
        FileInputStream inputStream=new FileInputStream(filepath);
        //将输入流转换为workbook
        @SuppressWarnings("resource")
		HSSFWorkbook workbook=new HSSFWorkbook(inputStream);
        //获取工作表
        HSSFSheet sheet=workbook.getSheetAt(0);
        int rowNum;
        if(num==0) {
        		rowNum=sheet.getLastRowNum();
        }
        else {
        		rowNum = num;
        }
//        int rowNum=sheet.getLastRowNum();
//        int rowNum = 1001;
        String[] LittleLabelData = new String[rowNum];
        for (int i=1;i<rowNum ; i++) {
                HSSFRow row=sheet.getRow(i);
                HSSFCell cell=row.getCell(3);
                String str = cell.getStringCellValue();
                LittleLabelData[i] = str;
        }
		return LittleLabelData;
	}
	
	
	
	public static String[] fromExcel2RegionArray(int num) throws IOException {
		String filepath = "测试数据1.xls";
        //读取excel文件 和读取其他文件没什么区别
        FileInputStream inputStream=new FileInputStream(filepath);
        //将输入流转换为workbook
        @SuppressWarnings("resource")
		HSSFWorkbook workbook=new HSSFWorkbook(inputStream);
        //获取工作表
        HSSFSheet sheet=workbook.getSheetAt(0);
        int rowNum;
        if(num==0) {
        		rowNum=sheet.getLastRowNum();
        }
        else {
        		rowNum = num;
        }
//        int rowNum=sheet.getLastRowNum();
//        int rowNum = 1001;
        String[] RegionData = new String[rowNum];
        for (int i=1;i<rowNum ; i++) {
                HSSFRow row=sheet.getRow(i);
                HSSFCell cell=row.getCell(0);
                String str = cell.getStringCellValue();
                RegionData[i] = str;
        }
		return RegionData;
	}
	
	public static String[] preProcess(String[] sheetData) {
		// 预处理
        for(int i=1;i<sheetData.length ; i++) {
         // 用正则表达式，同时匹配多个，这是在优化程序
            String rules = "(来话人反映)|(来话人)|(对此不满，)|(希望部门核实处理)|"
                    +"(希望部门调查处理。)|(请相关部门处理。)|(请相关部门处理)|(请处理。)|(严重)|(1\\d+T\\d+相同问题)|"
                    +"(认为不合理。)|(请相关部门调查处理。)|(其认为不合理\\。)"
                    +"|(从未得到解决)|(均未得到解决)|(未得到解决)|(^\\，)|(^\\。)|(问题仍未得到解决请处理)"
                    +"|(仍未解决)|(请处理)|(对此不满)"
					+"|(\\d+月)|(\\d+日)|(\\d+年)"
					+"|((\\d){1,2}:(\\d){2})|((\\d){1,2}：(\\d){2})"
					//因为只是针对区域的分类，可以大胆的去掉所有可以去掉的信息，以减少干扰
					//避免这种情形：两个信息因为有其他相同的信息而被判断为相识区域了，
					//比如时间、电话、请处理
					//当然，要意识到，之前之所以没引起大的问题，是因为使用了很多信息去训练
					//它提取了它们的相同值
					//起到了抑制作用
					+"|(\\d+月)|(\\d+日)|(\\d+年)"
					+"|(请相关)|(部门)|(核实)|(处理)"
					+"|(^左右)|(\\，$)|(\\。$)|(调查)|(^\\：)|(^其是)|(^是)|(^在)";
            Matcher m;
            do {
                Pattern r = Pattern.compile(rules);
                m = r.matcher(sheetData[i]);
                if(!m.find())break;
                Pattern p = Pattern.compile(m.group(0));
                Matcher matcher = p.matcher(sheetData[i]); 
                sheetData[i] = matcher.replaceAll("");
//              因为要提前判断m.find()了，才能继续下一步的执行，所以while里用true也是一样的  
            }while(m.find());     
        }//for

		return sheetData;
		
	}
	
	public static String textArray2SplitWordsArray(String[] sheetData,String[] LabelData,String[] LittleLabelData) {
		
		String text = "";
		String content = "";
		int len = sheetData.length;
		for(int i=1;i<len;i++) {
			sheetData[i] = (String.valueOf(NlpAnalysis.parse(sheetData[i])));
//			System.out.println("第"+i+"行："+sheetData[i]);
//			去掉数词
			Pattern p = Pattern.compile("\\d+年*月*日*/m\\,");
			Matcher matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\d+元*左右*/m\\,");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\d+元*左右*/m\\,");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\d+号*栋*/m\\,");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
			
//			去掉分词后面的词性标示，替换为空格
			String rules = "/[a-z]+\\,";
			p = Pattern.compile(rules);
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
			
//			去掉逗号、句号、结尾的。/w
			p = Pattern.compile("\\，");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\。");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("（");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("）");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("/w");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile(":");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\,");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\、");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\：");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\“");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
	        p = Pattern.compile("\\”");
			matcher = p.matcher(sheetData[i]); 
	        sheetData[i] = matcher.replaceAll("");
	        
//	        System.out.println("第"+i+"行："+sheetData[i]);
//	        System.out.println("text"+i+" = \"\"\""+sheetData[i]+"\"\"\"");
//	        System.out.println("text"+i+" = \"\"\""+"text"+i+" "+sheetData[i]+"\"\"\"");
//	        System.out.println(LabelData[i]+"|"+LittleLabelData[i]+"	"+"text"+i+" "+sheetData[i]);
//	        content += LabelData[i]+"|"+LittleLabelData[i]+"	"+"text"+i+" "+sheetData[i]+"\n";
	        if(i>1&&sheetData[i]==sheetData[i-1]){
				System.out.println(i+" 本条内容与上一条相同");
				} 
			else{
				content += LabelData[i]+"   "+"text"+i+" "+sheetData[i]+"\n";
				System.out.println(i);
				}
	        
//	        text += "text"+i+",";
		}
//		System.out.println(text);
//		return sheetData;
//		System.out.println(content) ;
		return content;
		
	}
	
public static String textArray2SplitWordsArray2(String[] sheetData,String[] RegionData) {
		
//		String text = "";
		String content = "";
		int j=0;
		for(int i=1;i<sheetData.length;i++) {
	        
	        if(i>1&&sheetData[i].equals(sheetData[i-1])){
				System.out.println(i+" 本条内容与上一条相同");
				j++;
				} 
			else{
				content += RegionData[i]+"    "+sheetData[i]+"\n";
				System.out.println(i);
				}
		}
		System.out.println("有"+j+"条重复信息") ;
		return content;
		
	}
	
	public static void contentToTxt(String filePath, String content) {  
        //现在讲这个写方法，修改为不保留原文本了
		//String str = new String(); //原有txt内容  
        String s1 = new String();//内容更新  
        try {  
            File f = new File(filePath);  
            if (f.exists()) {  
                System.out.println("文件已存在");  
            } else {  
                System.out.println("创建文件");  
                f.createNewFile();// 不存在则创建  
            }  
          //  BufferedReader input = new BufferedReader(new FileReader(f));  
  
            //while ((str = input.readLine()) != null) {  
//                s1 += str + "\n";  
  //          }  
		
            //System.out.println(s1);  
            //input.close();  
            s1 = content;  
  
            BufferedWriter output = new BufferedWriter(new FileWriter(f));  
            output.write(s1);  
            output.close();  
        } catch (Exception e) {  
            e.printStackTrace();  
  
        }  
    }  
	
	
	public static int[][] theAmountOfDiffs(String[] sheetData) {
		Set<String> set = new HashSet<String>();
		//List lst=new ArrayLis?
		
		for(int i=1;i<sheetData.length;i++) {
			String strarr[]=sheetData[i].split(",");
			for(int j=0;j<strarr.length;j++) {
				
				set.add(strarr[j]);
			}			
		}
		
		System.out.println("set.size(): "+set.size());
		
//		建立数组存储不重复的关键字
		String[] strtitle = new String [set.size()];
		int n = 0;
		for( Iterator   it = (Iterator) set.iterator();  it.hasNext(); ){   
			strtitle [n] = it.next().toString();
			n++;
//	    	System.out.println(it.next().toString());            
		} 
		
//		创建一个10*21的二维数组
		int[][] mainArray = new int[sheetData.length][set.size()];
		for(int i=0;i<sheetData.length;i++) {
			for(int j=0;j<set.size();j++) {
				mainArray[i][j]=0;
			}
		}
//		给整个10*21的矩阵赋值
		for(int i=1;i<sheetData.length;i++) {
//			System.out.println(sheetData[i]);
			String strarr[]=sheetData[i].split(",");
			for(int j=0;j<strtitle.length;j++) {
//				思路是：把默认坐标设置为0，拿关键字str[i][k]去对比，
//				只要有一个和维度关键字相等，就赋值为1，
//				如此一来可以加一个break的
				
				for(int k=0;k<strarr.length;k++) {
//					System.out.println(strarr[k]);
//					System.out.println(strtitle[j]);
//					System.out.println("");
//					System.out.println("");
					if(strarr[k].equals(strtitle[j])) {
//						System.out.println("相等");
						mainArray[i][j]=1;
						break;
					}
				}
//				if(mainArray[i][j]==1)break;
				
			}
		}
		
		
		return mainArray;
		
	}
	
	
public static void main(String[] args) throws IOException {
/**
 *
 *这个java文件就用来训练model
 *要使用很多的注释
 *使条理清晰、易读
 * 
 **/ 

 	wayOne();
	
	}

	//处理成“区域--内容”
	public static void wayOne() throws IOException {
		//处理所有文件 num为0
		int num = 0;
		//从excel读文件，只读来电内容部分
		String[] sheetData = fromExcel2TextArray(num);
		//进行一定的预处理，并不分词
		sheetData = preProcess(sheetData); 
		//获取区域数据
		String[] RegionLabelData = fromExcel2RegionArray(num);
		//组装内容
		String content = textArray2SplitWordsArray2(sheetData,RegionLabelData);
		//将内容写入文本
		contentToTxt("区域--内容.txt",content);

		//打印结束提示信息
		System.out.println("\"区域--内容\"格式");
		System.out.println("success!");
		}

	

}
