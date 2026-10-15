from fastapi import FastAPI

app = FastAPI(title="ShopFlow API")


@app.get("/customers")
def get_customers(limit: int = 2, offset: int = 0):
    users = [
        {
            "customer_id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "country": "USA",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "customer_id": 2,
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "country": "PT",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "customer_id": 3,
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
            "country": "ES",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "customer_id": 4,
            "name": "Bob Brown",
            "email": "bob.brown@example.com",
            "country": "UK",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "customer_id": 5,
            "name": "Charlie Davis",
            "email": "charlie.davis@example.com",
            "country": "US",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "customer_id": 6,
            "name": "Diana Wilson",
            "email": "diana.wilson@example.com",
            "country": "CA",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "customer_id": 7,
            "name": "Ethan Martinez",
            "email": "ethan.martinez@example.com",
            "country": "MX",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "customer_id": 8,
            "name": "Fiona Lee",
            "email": "fiona.lee@example.com",
            "country": "JP",
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        }
    ]
    return users[offset:offset + limit]

@app.get("/products")
def get_products(limit: int = 2, offset: int = 0):
    products = [
        {
            "product_id": 1,
            "name": "Product A",
            "category": "Category 1",
            "price": 19.99,
            "stock": 100,
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "product_id": 2,
            "name": "Product B",
            "category": "Category 2",
            "price": 29.99,
            "stock": 50,
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "product_id": 3,
            "name": "Product C",
            "category": "Category 3",
            "price": 9.99,
            "stock": 200,
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "product_id": 4,
            "name": "Product D",
            "category": "Category 1",
            "price": 14.99,
            "stock": 75,
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "product_id": 5,
            "name": "Product E",
            "category": "Category 2",
            "price": 39.99,
            "stock": 30,
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        }
    ]
    return products[offset:offset + limit]

@app.get("/orders")
def get_orders(limit: int = 2, offset: int = 0):
    orders = [
        {
            "order_id": 1,
            "customer_id": 1,
            "order_date": "2023-01-01T00:00:00Z",
            "status": "shipped",
            "total_amount": 69.97, 
            "updated_at": "2023-01-01T00:00:00Z",
            "items" : [
                {
                    "product_id": 1,
                    "quantity": 2,
                    "unit_price": 19.99
                },
                {
                    "product_id": 2,
                    "quantity": 1,
                    "unit_price": 29.99
                }
            ]
        },
        {
            "order_id": 2,
            "customer_id": 2,
            "order_date": "2023-01-02T00:00:00Z",
            "status": "processing",
            "total_amount": 49.98, 
            "updated_at": "2023-01-02T00:00:00Z",
            "items" : [
                {
                    "product_id": 3,
                    "quantity": 5,
                    "unit_price": 9.99
                }
            ]
        },
        {
            "order_id": 3,
            "customer_id": 3,
            "order_date": "2023-01-03T00:00:00Z",
            "status": "delivered",
            "total_amount": 44.97, 
            "updated_at": "2023-01-03T00:00:00Z",
            "items" : [
                {
                    "product_id": 4,
                    "quantity": 3,
                    "unit_price": 14.99
                }
            ]
        },
        {
            "order_id": 4,
            "customer_id": 1,
            "order_date": "2023-01-04T00:00:00Z",
            "status": "cancelled",
            "total_amount": 0.00, 
            "updated_at": "2023-01-04T00:00:00Z",
            "items" : []
        },
        {
            "order_id": 5,
            "customer_id": 2,
            "order_date": "2023-01-05T00:00:00Z",
            "status": "shipped",
            "total_amount": 79.98, 
            "updated_at": "2023-01-05T00:00:00Z",
            "items" : [
                {
                    "product_id": 5,
                    "quantity": 2,
                    "unit_price": 39.99
                }
            ]
        }
    ]
    return orders[offset:offset + limit]

@app.get("/payments")
def get_payments(limit: int = 2, offset: int = 0):
    payments = [
        {
            "payment_id": 1,
            "order_id": 1,
            "payment_method": "credit_card",
            "amount": 89.97,
            "status": "completed",
            "payment_date": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z"
        },
        {
            "payment_id": 2,
            "order_id": 2,
            "payment_method": "paypal",
            "amount": 49.98,
            "status": "pending",
            "payment_date": "2023-01-02T00:00:00Z",
            "updated_at": "2023-01-02T00:00:00Z"
        },
        {
            "payment_id": 3,
            "order_id": 3,
            "payment_method": "bank_transfer",
            "amount": 44.97,
            "status": "completed",
            "payment_date": "2023-01-03T00:00:00Z",
            "updated_at": "2023-01-03T00:00:00Z"
        },
        {
            "payment_id": 4,
            "order_id": 4,
            "payment_method": "credit_card",
            "amount": 0.00,
            "status": "failed",
            "payment_date": None,
            "updated_at": None
        },
        {
            "payment_id": 5,
            "order_id": 5,
            "payment_method": "paypal",
            "amount": 79.97,
            "status": "completed",
            "payment_date": "2023-01-05T00:00:00Z",
            "updated_at": "2023-01-05T00:00:00Z"
        }
    ]
    return payments[offset:offset + limit]



