from src.extract import extract_customers, extract_products, extract_orders, extract_payments
from src.storage import upload_json_async


def upload_to_minio_customers():
    customers = extract_customers()
    upload_json_async(data = customers, data_set="customers/customers.json")
    
def upload_to_minio_products():
    products = extract_products()
    upload_json_async(data = products, data_set="products/products.json")

def upload_to_minio_orders():
    orders = extract_orders()
    upload_json_async(data = orders, data_set="orders/orders.json")

def upload_to_minio_payments():
    payments = extract_payments()
    upload_json_async(data = payments, data_set="payments/payments.json") 

if __name__ == "__main__":
    upload_to_minio_customers()
    upload_to_minio_products()
    upload_to_minio_orders()
    upload_to_minio_payments()
    