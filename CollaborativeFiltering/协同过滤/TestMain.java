import java.io.IOException;
public class TestMain{
	public static void main(String[] args)throws IOException {
		String[][] strArr = Cf.controller("log.xls","10.158.46.78");
		Cf.printAllOfArr(strArr);
		


	}
}