import pandas
import numpy
from pyspark.sql import SparkSession
import pyspark.pandas


print(pyspark.__version__)

df = pandas.DataFrame({
    'a': [20,20,21],
    'b': [18,39,40]
     }
)

print(df)

### all is the same with Pandas API



