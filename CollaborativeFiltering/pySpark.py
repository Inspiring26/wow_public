#coding:utf-8
import spark

textFile = spark.read.text("result.txt")
textFile.count()