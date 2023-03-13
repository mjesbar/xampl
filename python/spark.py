from pyspark.sql import SparkSession
import pyspark.implicits._
import json


spark = SparkSession.builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.sparkContext.setLogLevel('INFO')") \
    .getOrCreate()

file = {
    "name": "John",
    "age": 30
}

file = json.dumps(file, indent=4)

open("test.json", "w").write(file)

df = spark.read.json("file:///home/debian/mega/github/xampl/python/test.json",
                     multiLine=True,
                     encoding="utf-8")

df.printSchema()
df .show()

df.select("name", "age").show()
print(type(df))



