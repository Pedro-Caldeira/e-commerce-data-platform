import os
import psycopg2
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pyspark.sql.functions import coalesce, col, lit, lower, to_timestamp, trim, explode, sum as spark_sum, when
from pyspark.sql.types import (
    ArrayType,
    StructType,
    StructField,
    DoubleType,
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
spark = (
    SparkSession.builder
    .appName("ShopFlowOrders")
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
order_items_schema = StructType([
    StructField("product_id", IntegerType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("unit_price", DoubleType(), True)
])
    
orders_schema = StructType([
    StructField("order_id", IntegerType(), False),  
    StructField("customer_id", IntegerType(), False),
    StructField("order_date", StringType(), True),
    StructField("status", StringType(), True),
    StructField("total_amount", DoubleType(), True),
    StructField("updated_at", StringType(), True),
    StructField("items", ArrayType(order_items_schema), True),
])

df_orders = (
      spark.read
        .schema(orders_schema)
        .option("multiline", "true")
        .json("s3a://shopflow-raw/orders/*.json")
    )
df_orders = df_orders.withColumn("order_date", to_timestamp("order_date")).withColumn("updated_at", to_timestamp("updated_at"))
df_order_items = (
    df_orders
    .select(
        "order_id",
        explode("items").alias("item")
    )
    .select(
        "order_id",
        "item.product_id",
        "item.quantity",
        "item.unit_price"
    )
)
df_order_items = (
    df_order_items
    .withColumn(
        "line_total",
        col("quantity") * col("unit_price")
    )
)
df_calculated_orders = (
    df_order_items
    .groupBy("order_id")
    .agg(
        spark_sum("line_total").alias("calculated_total")
    )
)
df_comparison = (
    df_orders
    .join(
        df_calculated_orders,
        on="order_id",
        how="left"
    )
    .withColumn(
        "calculated_total",
        coalesce(col("calculated_total"), lit(0.0))
    )
    .filter(col("total_amount") != col("calculated_total"))
    .select(
        "order_id",
        "calculated_total"
    )
)
df_orders = (
    df_orders
    .join(
        df_comparison,
        on="order_id",
        how="left"
    )
    .withColumn(
        "total_amount",
        when(
            col("calculated_total").isNotNull(),
            col("calculated_total")
        ).otherwise(
            col("total_amount")
        )
    )
    .drop("calculated_total")
)
everything_ok = df_orders.join(df_comparison, on="order_id", how="left").filter(col("calculated_total") != col("total_amount")).select("calculated_total","total_amount").show()

df_comparison.printSchema()
df_comparison.show(truncate=False)

df_orders.printSchema()
df_orders.show(truncate=False)

df_orders = df_orders.drop("items")

df_orders.write.jdbc(
    url=postgres_url,
    table="orders_staging",
    mode="overwrite",
    properties=postgres_properties
)

df_order_items.printSchema()
df_order_items.show(truncate=False)

df_order_items.write.jdbc(
    url=postgres_url,
    table="order_items_staging",
    mode="overwrite",
    properties=postgres_properties
)

conn = psycopg2.connect(
    host = os.getenv("POSTGRES_HOST"),
    port = os.getenv("POSTGRES_PORT"),
    database = os.getenv("POSTGRES_DB"),
    user = os.getenv("POSTGRES_USER"),
    password = os.getenv("POSTGRES_PASSWORD")
)
cursor = conn.cursor()

with open("sql/upsert_orders.sql", "r", encoding="utf-8") as file:
    upsert_orders_sql = file.read()

cursor.execute(upsert_orders_sql)

with open("sql/upsert_order_items.sql", "r", encoding="utf-8") as file:
    upsert_order_items_sql = file.read()

cursor.execute(upsert_order_items_sql)

conn.commit()
                                    
cursor.close()
conn.close()
spark.stop()    