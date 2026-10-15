from src.extract import extract_customers
from src.storage import upload_json



customers = extract_customers()
print(f"Extracted {len(customers)} customers")
upload_json(data=customers, object_name="customers/customers.json")

print("Uploaded customers to MinIO")
    
    