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
import org.ansj.splitWord.analysis.NlpAnalysis;
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.ansj.splitWord.analysis.NlpAnalysis;

public class Stat{
    public static String[] fromExcel2TextArray(int num) throws IOException {
        String filepath = "测试数据1.xls";
        //读取excel文件 和读取其他文件没什么区别
        FileInputStream inputStream=new FileInputStream(filepath);
        //将输入流转换为workbook
        HSSFWorkbook workbook=new HSSFWorkbook(inputStream);
        //获取工作表
        HSSFSheet sheet=workbook.getSheetAt(0);
        int rowNum;
        if(num==-1){
            rowNum=sheet.getLastRowNum();
        }
        else{
            rowNum = num;
        }

        String[] sheetData = new String[rowNum];

        for (int i=1;i<rowNum ; i++) {
            HSSFRow row=sheet.getRow(i);
            HSSFCell cell=row.getCell(0);
            String str = cell.getStringCellValue();
            sheetData[i] = str;
        
        }
        return sheetData;
    }
    

    public static String[] assemble(String[] sheetData){
        Set<String> set = new HashSet<String>();
        for(int i=1;i<sheetData.length;i++){
            set.add(sheetData[i]);
        } 
        System.out.println("set.size(): "+set.size());
        String[] strtitle = new String [set.size()];
        int n=0;
        for( Iterator   it = (Iterator) set.iterator();  it.hasNext(); ){
            strtitle [n] = it.next().toString();
            n++;
        }
        return strtitle;
    }

    public static void main(String[] args) throws IOException{
        int num = -1;
        String[] sheetData = fromExcel2TextArray(num);
        String[] strtitle = assemble(sheetData);           
        for(int i=0;i<strtitle.length;i++){
            //System.out.println(i+" :"+strtitle[i]);
            System.out.print("|("+strtitle[i]+")");
        }
    }


}
