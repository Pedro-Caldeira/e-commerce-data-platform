from minio import Minio
from dotenv import load_dotenv
import os


load_dotenv()

print("HOST:", os.getenv("MINIO_HOST"))
print("SECURE:", os.getenv("MINIO_SECURE"))


client = Minio(
    os.getenv("MINIO_HOST"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

print(client.list_buckets())