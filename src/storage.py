import io
import json
import os

from src.validation import validate_data
from dotenv import load_dotenv
from minio import Minio
from datetime import datetime
import hashlib

load_dotenv()


def get_minio_client() -> Minio:
    return Minio(
        os.getenv("MINIO_HOST"),
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False
    )
def generate_object_name(dataset: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{dataset}/{dataset}_{timestamp}.json"

def generate_batch_id(data:list[dict], dataset:str, primary_key:str):
    ids = sorted(item[primary_key] for item in data)
    raw = f"{dataset}:{",".join(map(str,ids))}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]

def generate_idempotent_object_name(
    data: list[dict],
    dataset: str,
    primary_key: str
) -> str:

    batch_id = generate_batch_id(
        data=data,
        dataset=dataset,
        primary_key=primary_key
    )

    return f"{dataset}/{dataset}_{batch_id}.json"

def upload_json(data: list[dict], dataset: str, primary_key:str) -> None:
    client = get_minio_client()
    object_name = generate_idempotent_object_name(data,dataset,primary_key)
    
    json_data = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
    client.put_object(
        bucket_name=os.getenv("MINIO_BUCKET"),
        object_name=object_name,
        data=io.BytesIO(json_data),
        length=len(json_data),
        content_type="application/json"
    )

def upload_json_async(data: list[dict], data_set: str) -> None:
    primary_keys = {
    "customers": "customer_id",
    "products": "product_id",
    "orders": "order_id",
    "payments": "payment_id"
    }
    dataset = data_set.split("/")[0]
    primary_key = primary_keys[dataset]
    valid_data,invalid_data = validate_data(data,dataset)
    processed_data = deduplicate_data(valid_data,dataset)
    last_processed_id = load_watermark(dataset)
    
    if (invalid_data):
        print(f"Dados inválidos encontrados para {dataset}:")
        upload_quarantine(invalid_data,dataset)

    if(last_processed_id is None):
        last_processed_id = 0
        save_watermark(dataset, 0)
    
    new_data = []
    for item in processed_data:
        if item.get(primary_key, 0) > last_processed_id:
            new_data.append(item)
            
    if not new_data:
        print(f"Nenhum dado novo para {dataset}")
        return
    
    try:   
        upload_json(new_data,dataset,primary_key)
        
        last_id = max(
            item.get(primary_key, 0)
            for item in new_data
        )


        print(f"Last processed ID for {dataset}: {last_id}")

        save_watermark(dataset,last_id)

    except Exception as e:
        print(
            f"Erro no processamento de {dataset}: {e}"
        )
        raise

def save_watermark(dataset:str, last_processed_id:int) -> None:
    client = get_minio_client()
    watermark_data = {"last_processed_id": last_processed_id}
    json_data = json.dumps(watermark_data, ensure_ascii=False, indent=2).encode("utf-8")
    client.put_object(
        bucket_name=os.getenv("MINIO_BUCKET"),
        object_name=f"watermarks/{dataset}_watermark.json",
        data=io.BytesIO(json_data),
        length=len(json_data),
        content_type="application/json"
    )   
def load_watermark(dataset: str) -> int | None:
    client = get_minio_client()

    try:
        response = client.get_object(
            bucket_name=os.getenv("MINIO_BUCKET"),
            object_name=f"watermarks/{dataset}_watermark.json"
        )

        watermark_data = json.loads(
            response.read().decode("utf-8")
        )

        return watermark_data.get("last_processed_id", 0)

    except Exception as e:
        print(f"Error loading watermark for dataset {dataset}: {e}")
        return None

def deduplicate_data(data: list[dict],dataset:str) -> list[dict]:
    primary_keys = {
        "customers": "customer_id",
        "products": "product_id",
        "orders": "order_id",
        "payments": "payment_id"
    }
    unique_data_id = []
    correct_data = []
    for item in data:
        id = item[primary_keys[dataset]]
        if id  not in unique_data_id:
            unique_data_id.append(id) 
            correct_data.append(item)
    return correct_data

def upload_quarantine(invalid_data:list[dict], dataset:str):
    client = get_minio_client()

    if(invalid_data):
        json_data = json.dumps(invalid_data,ensure_ascii=False,indent=2).encode("utf-8")
        client.put_object(
                bucket_name = os.getenv("MINIO_BUCKET"),
                object_name = f"quarantine/{dataset}_quarantine.json",
                data = io.BytesIO(json_data),
                length = len(json_data),
                content_type = "application/json"
            )
        
