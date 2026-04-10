from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, col, to_timestamp

spark = SparkSession.builder.appName("RideTransform").getOrCreate()

df = spark.read.option("header", True).csv(
    "gs://ride-data-lake-123/raw/trips/"
)

# Convert ingestion_time to timestamp
df = df.withColumn(
    "ingestion_time",
    to_timestamp(col("ingestion_time"))
)

# Add processed_time
df = df.withColumn("processed_time", current_timestamp())

df.write.mode("overwrite").parquet(
    "gs://ride-data-lake-123/processed/trips/"
)