object ScalaCF{
	/*基于分布式的协同过滤系统
	 *
	 *
	 */
	def printHello(): Unit = {
		println("Hello")


	}

	def readFileAndCount(): Unit = {
		import org.apache.spark
		val textFile = spark.read.textFile("result.txt")
		println(textFile.count())
	}
	def main(args: Array[String]){
		printHello()
	}
}