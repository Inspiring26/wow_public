import java.io.BufferedReader; 
import java.io.InputStreamReader;
public class Testpj{
	public static void main(String[] args)throws Exception {
		Process pr = Runtime.getRuntime().exec("python testpj.py 123");
		//获取python文件运行后的输出
		BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
		String line;
		while ((line = in.readLine()) != null) {

			System.out.println(line);

		}
		in.close();
		pr.waitFor();
		System.out.println("sucecss!");
	}
}