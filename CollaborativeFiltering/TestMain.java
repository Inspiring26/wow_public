import java.io.IOException;
public class TestMain{
	public static void main(String[] args)throws IOException {
		String[][] strArr = Cf.controller("log.xls","10.158.48.68");
		Cf.printAllOfArr(strArr);
		
	}
}