import os
import psycopg2
from dotenv import load_dotenv
from pyspark.sql import SparkSession 
from pyspark.sql.functions import lower, to_timestamp, trim
from pyspark.sql.types import (
    DoubleType,
    StructType,
    StructField,
    IntegerType,
    StringType,
)

load_dotenv()
postgres_url = f"jdbc:postgresql://{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

postgres_properties = {
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "driver": "org.postgresql.Driver"
}

products_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("category", StringType(), True),
    StructField("price", DoubleType(), False),
    StructField("stock", IntegerType(), False),
    StructField("created_at", StringType(), True),
    StructField("updated_at", StringType(), True),
])

spark = (
    SparkSession.builder
    .appName("ShopFlowProducts")
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

df_products = (
    spark.read
    .schema(products_schema)
    .option("multiline", "true")
    .json("s3a://shopflow-raw/products/*.json")
)

df_products = df_products.withColumn("created_at", to_timestamp("created_at")).withColumn("updated_at", to_timestamp("updated_at"))
df_products = (
    df_products
    .withColumn("name", trim("name"))
    .withColumn("category", trim("category"))
)
df_products.printSchema()
df_products.show(truncate=False)

df_products.write.jdbc(
    url=postgres_url,
    table="products_staging",
    mode="overwrite",
    properties=postgres_properties
)

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)
cursor = conn.cursor()
file = open("e-commerce_data_platform/sql/products_upsert.sql", "r", encoding="utf-8")
sql = file.read()
cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()
spark.stop()
