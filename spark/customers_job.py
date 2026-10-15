import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, to_timestamp, trim
import psycopg2

from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    TimestampType
)
load_dotenv()
postgres_url = f"jdbc:postgresql://{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

postgres_properties = {
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "driver": "org.postgresql.Driver"
}

customers_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("email", StringType(), False),
    StructField("country", StringType(), True),
    StructField("created_at", StringType(), True),
    StructField("updated_at", StringType(), True),
])

spark = (
    SparkSession.builder
    .appName("ShopFlowCustomers")
    .master("local[*]")
    .config(
    "spark.jars.packages",
    "org.apache.hadoop:hadoop-aws:3.5.0,"
    "org.postgresql:postgresql:42.7.7"
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

df_customers = (
    spark.read
    .schema(customers_schema)
    .option("multiline", "true")
    .json("s3a://shopflow-raw/customers/*.json")
)
df_customers = df_customers.withColumn("created_at", to_timestamp("created_at")).withColumn("updated_at", to_timestamp("updated_at"))
df_customers = df_customers.withColumn("email", lower(trim("email")))


print("Postgres user:", postgres_properties["user"])
print("Password length:", len(postgres_properties["password"]))
print("JDBC URL:", postgres_url)

df_customers.write.jdbc(
    url=postgres_url,
    table="customers",
    mode="append",
    properties=postgres_properties
)


spark.stop()