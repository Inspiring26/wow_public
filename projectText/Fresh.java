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


public class Fresh{
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
                +"|(^左右)|(\\，$)|(\\。$)|(调查)|(^\\：)|(^其是)|(^是)|(^在)|(^，)"
                +"|(深夜)|(施工)|(噪音)|(扰民)|(近期)|(司机)|(不满)";
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
	        
	        content += LabelData[i]+"	"+"text"+i+" "+sheetData[i]+"\n";
	        System.out.println(i);
	        
		}
		return content;
		
	}
	
public static String textArray2SplitWordsArray2(String[] sheetData,String[] RegionData) {
	    int j=0;	
		String content = "";
		for(int i=1;i<sheetData.length;i++) {
	        if(sheetData[i].equals(sheetData[i-1])&&i>1){
                j++;
                continue;
            }    
	        content += RegionData[i]+"	"+" "+sheetData[i]+"\n";
	        System.out.println(i);
		}
        System.out.println("有"+j+"条重复信息。已删除。");
		return content;
		
	}

    public static String assemble(String[] sheetData,String[] RegionData){
        String content = "";
        for(int i=1;i<sheetData.length;i++){
            if(sheetData[i].equals(sheetData[i-1])&&i>1){
                System.out.println(i+" 本条内容与上一条相同");
            }
            else{
                content += RegionData[i]+"  "+" "+sheetData[i]+"\n";
                System.out.println(i);
            }
        }
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
    //       BufferedReader input = new BufferedReader(new FileReader(f));  
  //
    //        while ((str = input.readLine()) != null) {  
      //          s1 += str + "\n";  
        //    }  
         //   System.out.println(s1);  
          //  input.close();  
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
			String strarr[]=sheetData[i].split(",");
			for(int j=0;j<strtitle.length;j++) {
//				思路是：把默认坐标设置为0，拿关键字str[i][k]去对比，
//				只要有一个和维度关键字相等，就赋值为1，
//				如此一来可以加一个break的
				
				for(int k=0;k<strarr.length;k++) {
					if(strarr[k].equals(strtitle[j])) {
						mainArray[i][j]=1;
						break;
					}
				}
				
			}
		}
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
    //String content = assemble(sheetData,RegionLabelData);
    String content = textArray2SplitWordsArray2(sheetData,RegionLabelData);
    
    contentToTxt("region.txt",content);
    System.out.println("success!");
    
	
	}

	

}

