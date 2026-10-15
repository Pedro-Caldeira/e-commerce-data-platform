import os

from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()

spark = (
    SparkSession.builder
    .appName("ShopFlowMinIO")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.5.0"
    )
    .config(
        "spark.hadoop.fs.s3a.endpoint",
        f"http://{os.getenv('MINIO_HOST')}"
    )
    .config(
        "spark.hadoop.fs.s3a.access.key",
        os.getenv("MINIO_ACCESS_KEY")
    )
    .config(
        "spark.hadoop.fs.s3a.secret.key",
        os.getenv("MINIO_SECRET_KEY")
    )
    .config(
        "spark.hadoop.fs.s3a.path.style.access",
        "true"
    )
    .config(
        "spark.hadoop.fs.s3a.connection.ssl.enabled",
        "false"
    )
    .config(
        "spark.hadoop.fs.s3a.impl",
        "org.apache.hadoop.fs.s3a.S3AFileSystem"
    )
    .getOrCreate()
)

print("Spark:", spark.version)
print(
    "Hadoop:",
    spark.sparkContext._jvm.org.apache.hadoop.util.VersionInfo.getVersion()
)

df = (
    spark.read
    .option("multiline", "true")
    .json("s3a://shopflow-raw/customers/*.json")
)

df.show(truncate=False)

spark.stop()