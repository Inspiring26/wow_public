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


public class TextPreprocess {
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
            String rules_old = "(来话人反映)|(来话人)|(对此不满，)|(希望部门核实处理)|"
                    +"(希望部门调查处理。)|(请相关部门处理。)|(请相关部门处理)|(请处理。)|(严重)|(1\\d+T\\d+相同问题)|"
                    +"(认为不合理。)|(请相关部门调查处理。)|(其认为不合理\\。)"
                    +"|(从未得到解决)|(均未得到解决)|(未得到解决)|(^\\，)|(^\\。)|(问题仍未得到解决请处理)"
                    +"|(仍未解决)|(请处理)|(对此不满)";
           String rules =  "(来话人)|(反映)|(对此不满，)|(希望)|(请)|(部门)|(核实)|(处理)"
                +"|(调查)|(相关)|(严重)|(1\\d+T\\d+相同问题)"
                +"|(\\d+月)|(\\d+日)|(\\d+年)"
                +"|((\\d){1,2}:(\\d){2})|((\\d){1,2}：(\\d){2})"
                +"|(^左右)|(\\，$)|(\\。$)|(调查)|(^\\：)|(^其是)|(^是)|(^在)|(^，)";
           // 进一步优化，只有当mMatch2.group(0):null时才停止循环，
           // 有些信息需要处理掉很多信息，需要处理很多次的，
           // 比如
           // 19--0--mMatch2.group(0):来话人反映
           // 19--0--mMatch2.group(1):来话人反映
           // 19--1--mMatch2.group(0):170608T00282相同问题
           // 19--1--mMatch2.group(1):null
           // 19--2--mMatch2.group(0):，
           // 19--2--mMatch2.group(1):null
           // 19--3--mMatch2.group(0):严重
           // 19--3--mMatch2.group(1):null
           // 19--4--mMatch2.group(0):来话人
           // 19--4--mMatch2.group(1):null
           // 19--5--mMatch2.group(0):问题仍未得到解决请处理
           // 19--5--mMatch2.group(1):null
           // 19--6--mMatch2.group(0):希望部门核实处理
           // 19--6--mMatch2.group(1):null
           // 处理了七次，还有要删掉的词
           // do...while循环来替代for循环
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
		for(int i=1;i<sheetData.length;i++) {
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
	        
	        content += LabelData[i]+"	"+"text"+i+" "+sheetData[i]+"\n";
//	        System.out.println(LabelData[i]+" "+sheetData[i]);
//			System.out.println("");
	        System.out.println(i);
	        
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
		for(int i=1;i<sheetData.length;i++) {
//			sheetData[i] = (String.valueOf(NlpAnalysis.parse(sheetData[i])));
////			System.out.println("第"+i+"行："+sheetData[i]);
////			去掉数词
//			Pattern p = Pattern.compile("\\d+年*月*日*/m\\,");
//			Matcher matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\d+元*左右*/m\\,");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\d+元*左右*/m\\,");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\d+号*栋*/m\\,");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//			
////			去掉分词后面的词性标示，替换为空格
//			String rules = "/[a-z]+\\,";
//			p = Pattern.compile(rules);
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//			
////			去掉逗号、句号、结尾的。/w
//			p = Pattern.compile("\\，");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\。");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("（");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("）");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("/w");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile(":");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\,");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\、");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\：");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\“");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
//	        
//	        p = Pattern.compile("\\”");
//			matcher = p.matcher(sheetData[i]); 
//	        sheetData[i] = matcher.replaceAll("");
	        
//	        System.out.println("第"+i+"行："+sheetData[i]);
//	        System.out.println("text"+i+" = \"\"\""+sheetData[i]+"\"\"\"");
//	        System.out.println("text"+i+" = \"\"\""+"text"+i+" "+sheetData[i]+"\"\"\"");
//	        System.out.println(LabelData[i]+"|"+LittleLabelData[i]+"	"+"text"+i+" "+sheetData[i]);
//	        content += LabelData[i]+"|"+LittleLabelData[i]+"	"+"text"+i+" "+sheetData[i]+"\n";
	        
	        content += RegionData[i]+"	"+" "+sheetData[i]+"\n";
//	        System.out.println(LabelData[i]+" "+sheetData[i]);
//			System.out.println("");
	        System.out.println(i);
	        
//	        text += "text"+i+",";
		}
//		System.out.println(text);
//		return sheetData;
//		System.out.println(content) ;
		return content;
		
	}
	
	public static void contentToTxt(String filePath, String content) {  
        String str = new String(); //原有txt内容  
        String s1 = new String();//内容更新  
        try {  
            File f = new File(filePath);  
            if (f.exists()) {  
                System.out.print("文件存在");  
            } else {  
                System.out.print("创建文件");  
                f.createNewFile();// 不存在则创建  
            }  
            BufferedReader input = new BufferedReader(new FileReader(f));  
  
            while ((str = input.readLine()) != null) {  
                s1 += str + "\n";  
            }  
            System.out.println(s1);  
            input.close();  
            s1 += content;  
  
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
//		
//		for(int i=1;i<mainArray.length;i++) {
//			System.out.println("第"+i+"行：");
//			for(int j=0;j<mainArray[1].length;j++) {
//				System.out.print(mainArray[i][j]+" ");
//			}
//			System.out.println("");
//		}
//		
		
		
		return mainArray;
		
	}
	
	
public static void main(String[] args) throws IOException {
//	如果num=0，则默认为所有的行
//	否则为指定的行数
	int num=0;
	String[] sheetData = fromExcel2TextArray(num);
//	String[] LabelData = fromExcel2LabelArray(num);
//	String[] LittleLabelData = fromExcel2LittleLabelArray(num);
	String[] RegionLabelData = fromExcel2RegionArray(num);
    
	
    sheetData = preProcess(sheetData); 
   
//    String content = textArray2SplitWordsArray2(sheetData,LabelData,LittleLabelData); 
    String content = textArray2SplitWordsArray2(sheetData,RegionLabelData);
    
    contentToTxt("region.txt",content);
    System.out.println("success!");
    
//	theAmountOfDiffs(sheetData);
	
//	System.out.println("深夜/t"=="深夜/t");
	}

	

}

