## 파이썬 예제 2 - 고수준

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg 

# SparkSession으로부터 데이터프레임을 만듬 
spark = (SparkSession
         .builder
         .appName("AuthorAges")
         .getOrCreate())

# 데이터 프레임 생성
data_df = spark.createDataFrame([("Brooke", 20), ("Denny", 31), ("Jules", 30), ("TD", 35), ("Brooke", 25)], ["name", "age"])

# 동일한 이름으로 그룹화하여 나이별로 계산해 평균을 구함
avg_df = data_df.groupby("name").agg(avg("age"))

# 최종 실행 결과를 보여줌
print(avg_df.show())