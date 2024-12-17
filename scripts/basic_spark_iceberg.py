from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions as F
from pyspark.sql.types import *

from spark_config_iceberg import create_spark_session
spark = create_spark_session()
spark.sql("show databases").show()

def IngestIcebergCSVHeader(iDBSchema, iTable, iFilePath):
    csv_df = spark.read \
        .option("header", True) \
        .option("inferSchema", True) \
        .csv(iFilePath)

    print("Sample data from CSV:")
    csv_df.show()

    print("DataFrame Schema:")
    csv_df.printSchema()
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {iDBSchema}")


    csv_df.write \
        .format("iceberg") \
        .mode("overwrite") \
        .option("write.format.default", "parquet") \
        .option("write.metadata.compression-codec", "gzip") \
        .partitionBy("passenger_count") \
        .saveAsTable(f"{iDBSchema}.{iTable}")

IngestIcebergCSVHeader(
    "taxi_data",
    "yellow_trips",
    "s3a://source-data/yellow_tripdata_2016-01.csv"
)


print("\nTable properties:")
spark.sql("SHOW TABLES IN taxi_data").show()

