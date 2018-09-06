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
public class NewWrite{
	//文件名
	static String file = "测试数据1.xls";
	//读取excel行数，-1代表读取所有
	static int num = 10000;

	public static String[][] getExcel()throws IOException{
		FileInputStream fis = new FileInputStream(file);
		//将输入流转换为workbook
		HSSFWorkbook wb = new HSSFWorkbook(fis);
		//指定sheet
		HSSFSheet sheet = wb.getSheetAt(0);
		int rowNum;
		if(num==-1){
            //知道为什么行数有问题了
            //这是由于poi的机制问题，getLastRowNum()获得的是最后一行的航标，不是行数
            //而excel的机制是从第0行开始计算的
			rowNum = sheet.getLastRowNum()+1;
		}	
		else{
			rowNum = num;
		}
		String[][] sheetData = new String[rowNum][4];
		//定义for循环中要用到的变量
		HSSFRow row;
		HSSFCell cell;
		String str;
		for(int i=0;i<rowNum;i++){
			row = sheet.getRow(i);
			for(int j=0;j<4;j++){
				cell = row.getCell(j);
				str = cell.getStringCellValue();
				sheetData[i][j] = str;
			}
		}
		return sheetData;
	}
    public static String[][] filter(String[][] str){
        //正则表达式规则
        String rule =  "(来话人)|(反映)|(对此不满，)|(希望)|(请)|(部门)|(核实)|(处理)"
            +"|(调查)|(相关)|(严重)|(1\\d+T\\d+相同问题)" 
			+"|(\\d+月)|(\\d+日)|(\\d+年)"
			+"|((\\d){1,2}:(\\d){2})|((\\d){1,2}：(\\d){2})"
			+"|(^左右)|(\\，$)|(\\。$)|(调查)|(^\\：)|(^其是)|(^是)|(^在)|(^，)";
        //声明循环中要用到的变量
        Matcher m;
        Pattern r;//用于查找匹配词
        Pattern p;//用于匹配替换
        Matcher mc;
        for(int i=1;i<str.length;i++){
            do{
                //寻找匹配项
                r = Pattern.compile(rule);
                m = r.matcher(str[i][1]);

                if(!m.find())break;

                p = Pattern.compile(m.group(0));
                mc = p.matcher(str[i][1]);
                str[i][1] = mc.replaceAll("");
            }while(m.find());
        }    
        return str;
    }    

    public static String assemble(String[][] str){
        String content = "";
        int j=0;
        for(int i=1;i<str.length;i++){
            if(str[i][1].equals(str[i-1][1])){
                System.out.println(i+" 本条内容与上一条相同");
                j++;
            }
            else{
                content += str[i][0]+"  "+str[i][1]+"\n";
                System.out.println(i);
            }
        }
        System.out.println("有"+j+"条重复信息");
        return content;

    }

    public static String assemble2(String[][] str){
        String content = "";
        for(int i=1;i<str.length;i++){
            content += str[i][0]+"  "+str[i][1]+"\n";
            System.out.println(i);
        }
        return content;
    }

    public static void write(String str,String p)throws IOException{
        try{
            File f = new File(p);
            if(f.exists()){
                System.out.println("指定文件名的文件已存在,将覆盖原文件");
            }
            else{
                System.out.println("创建文件");
                f.createNewFile();
            }
            
            BufferedWriter output = new BufferedWriter(new FileWriter(f));
            output.write(str);
            output.close();
        }catch(Exception e){
            e.printStackTrace();
        }

    }


	public static void main(String[] args)throws IOException{
        //获取训练集所有信息，存为二维数组
		String[][] sheetData = getExcel();
        //打印二维数组长度
		System.out.println(sheetData.length);
        //过滤
        sheetData = filter(sheetData);
        //得到指定格式内容
        String content = assemble2(sheetData);
        //将内容写入文件
        write(content,"region.txt");
	}
}
