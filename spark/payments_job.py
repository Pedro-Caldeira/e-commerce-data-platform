import pyspark
import psycopg2
import os
from dotenv import load_dotenv
from pyspark.sql.functions import lower, to_timestamp, trim, sum as spark_sum
from pyspark.sql.types import (
    StructType,
    StructField,
    DoubleType,
    IntegerType,
    StringType,
)

load_dotenv()

payments_schema = StructType([
    StructField("payment_id", IntegerType(), False),
    StructField("order_id", IntegerType(), False),
    StructField("payment_method", StringType(), True),
    StructField("amount", DoubleType(), False),
    StructField("status", StringType(), True),
    StructField("payment_date", StringType(), True),
    StructField("updated_at", StringType(), True),
])

postgres_url = f"jdbc:postgresql://{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

postgres_properties = {
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "driver": "org.postgresql.Driver"
}

spark = (
    pyspark.sql.SparkSession.builder
    .appName("ShopFlowPayments")
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

df_payments = (
    spark.read
    .schema(payments_schema)
    .option("multiline", "true")
    .json("s3a://shopflow-raw/payments/*.json")
)

df_payments = df_payments.withColumn("payment_date", to_timestamp("payment_date")).withColumn("updated_at", to_timestamp("updated_at"))
df_payments = df_payments.withColumn("payment_method", lower(trim("payment_method"))).withColumn("status", lower(trim("status")))


print("Configuração PostgreSQL:")
print("Host:", os.getenv("POSTGRES_HOST"))
print("Porta:", os.getenv("POSTGRES_PORT"))
print("Base de dados:", os.getenv("POSTGRES_DB"))
print("Utilizador:", os.getenv("POSTGRES_USER"))


print("Número de pagamentos escritos:", df_payments.count())
df_payments.show(truncate=False)

print("A escrever na tabela payments...")

df_payments.write.jdbc(
    url=postgres_url,
    table="payments_staging",
    mode="overwrite",
    properties=postgres_properties
)

print("Escrita JDBC concluída com sucesso.")

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)
cursor = conn.cursor()
file = open("sql/upsert_payments.sql", "r", encoding="utf-8")
sql = file.read()
cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()
spark.stop()



