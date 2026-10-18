from fastapi import FastAPI

app = FastAPI(title="ShopFlow API")


@app.get("/customers")
def get_customers(limit: int = 5, offset: int = 0):
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
        },
        {
            "customer_id": 9,
            "name": "George Clark",
            "email": "george.clark@example.com",
            "country": "UK",
            "created_at": "2023-01-10T09:30:00Z",
            "updated_at": "2023-01-10T09:30:00Z"
        },
        {
            "customer_id": 10,
            "name": "Hannah Lewis",
            "email": "hannah.lewis@example.com",
            "country": "US",
            "created_at": "2023-01-12T14:15:00Z",
            "updated_at": "2023-01-12T14:15:00Z"
        },
        {
            "customer_id": 11,
            "name": "Jo\u00e3o Silva",
            "email": "joao.silva@example.com",
            "country": "PT",
            "created_at": "2023-01-15T11:20:00Z",
            "updated_at": "2023-01-15T11:20:00Z"
        },
        {
            "customer_id": 12,
            "name": "Maria Santos",
            "email": "maria.santos@example.com",
            "country": "PT",
            "created_at": "2023-01-18T16:45:00Z",
            "updated_at": "2023-01-18T16:45:00Z"
        },
        {
            "customer_id": 13,
            "name": "Pedro Ferreira",
            "email": "pedro.ferreira@example.com",
            "country": "PT",
            "created_at": "2023-01-20T10:00:00Z",
            "updated_at": "2023-01-20T10:00:00Z"
        },
        {
            "customer_id": 14,
            "name": "Ana Oliveira",
            "email": "ana.oliveira@example.com",
            "country": "PT",
            "created_at": "2023-01-22T08:30:00Z",
            "updated_at": "2023-01-22T08:30:00Z"
        },
        {
            "customer_id": 15,
            "name": "Carlos Rodriguez",
            "email": "carlos.rodriguez@example.com",
            "country": "ES",
            "created_at": "2023-01-25T13:10:00Z",
            "updated_at": "2023-01-25T13:10:00Z"
        },
        {
            "customer_id": 16,
            "name": "Elena Gomez",
            "email": "elena.gomez@example.com",
            "country": "ES",
            "created_at": "2023-01-28T17:50:00Z",
            "updated_at": "2023-01-28T17:50:00Z"
        },
        {
            "customer_id": 17,
            "name": "Lucas Martin",
            "email": "lucas.martin@example.com",
            "country": "FR",
            "created_at": "2023-02-01T09:00:00Z",
            "updated_at": "2023-02-01T09:00:00Z"
        },
        {
            "customer_id": 18,
            "name": "Camille Bernard",
            "email": "camille.bernard@example.com",
            "country": "FR",
            "created_at": "2023-02-03T15:25:00Z",
            "updated_at": "2023-02-03T15:25:00Z"
        },
        {
            "customer_id": 19,
            "name": "Lukas Schmidt",
            "email": "lukas.schmidt@example.com",
            "country": "DE",
            "created_at": "2023-02-06T12:40:00Z",
            "updated_at": "2023-02-06T12:40:00Z"
        },
        {
            "customer_id": 20,
            "name": "Sophie Weber",
            "email": "sophie.weber@example.com",
            "country": "DE",
            "created_at": "2023-02-08T18:15:00Z",
            "updated_at": "2023-02-08T18:15:00Z"
        },
        {
            "customer_id": 21,
            "name": "Marco Rossi",
            "email": "marco.rossi@example.com",
            "country": "IT",
            "created_at": "2023-02-11T10:50:00Z",
            "updated_at": "2023-02-11T10:50:00Z"
        },
        {
            "customer_id": 22,
            "name": "Giulia Bianchi",
            "email": "giulia.bianchi@example.com",
            "country": "IT",
            "created_at": "2023-02-14T14:30:00Z",
            "updated_at": "2023-02-14T14:30:00Z"
        },
        {
            "customer_id": 23,
            "name": "Liam O'Connor",
            "email": "liam.oconnor@example.com",
            "country": "IE",
            "created_at": "2023-02-17T11:05:00Z",
            "updated_at": "2023-02-17T11:05:00Z"
        },
        {
            "customer_id": 24,
            "name": "Siobhan Murphy",
            "email": "siobhan.murphy@example.com",
            "country": "IE",
            "created_at": "2023-02-20T16:20:00Z",
            "updated_at": "2023-02-20T16:20:00Z"
        },
        {
            "customer_id": 25,
            "name": "Lars Jansen",
            "email": "lars.jansen@example.com",
            "country": "NL",
            "created_at": "2023-02-23T09:45:00Z",
            "updated_at": "2023-02-23T09:45:00Z"
        },
        {
            "customer_id": 26,
            "name": "Emma Van Dijk",
            "email": "emma.vandijk@example.com",
            "country": "NL",
            "created_at": "2023-02-26T13:35:00Z",
            "updated_at": "2023-02-26T13:35:00Z"
        },
        {
            "customer_id": 27,
            "name": "Tiago Costa",
            "email": "tiago.costa@example.com",
            "country": "BR",
            "created_at": "2023-03-01T15:10:00Z",
            "updated_at": "2023-03-01T15:10:00Z"
        },
        {
            "customer_id": 28,
            "name": "Beatriz Souza",
            "email": "beatriz.souza@example.com",
            "country": "BR",
            "created_at": "2023-03-04T18:25:00Z",
            "updated_at": "2023-03-04T18:25:00Z"
        },
        {
            "customer_id": 29,
            "name": "Gabriel Lima",
            "email": "gabriel.lima@example.com",
            "country": "BR",
            "created_at": "2023-03-07T12:00:00Z",
            "updated_at": "2023-03-07T12:00:00Z"
        },
        {
            "customer_id": 30,
            "name": "Kenji Sato",
            "email": "kenji.sato@example.com",
            "country": "JP",
            "created_at": "2023-03-10T08:15:00Z",
            "updated_at": "2023-03-10T08:15:00Z"
        },
        {
            "customer_id": 31,
            "name": "Yuki Tanaka",
            "email": "yuki.tanaka@example.com",
            "country": "JP",
            "created_at": "2023-03-13T14:40:00Z",
            "updated_at": "2023-03-13T14:40:00Z"
        },
        {
            "customer_id": 32,
            "name": "Oliver Smith",
            "email": "oliver.smith@example.com",
            "country": "UK",
            "created_at": "2023-03-16T10:20:00Z",
            "updated_at": "2023-03-16T10:20:00Z"
        },
        {
            "customer_id": 33,
            "name": "Charlotte Jones",
            "email": "charlotte.jones@example.com",
            "country": "UK",
            "created_at": "2023-03-19T17:05:00Z",
            "updated_at": "2023-03-19T17:05:00Z"
        },
        {
            "customer_id": 34,
            "name": "Alexander Wright",
            "email": "alexander.wright@example.com",
            "country": "US",
            "created_at": "2023-03-22T11:50:00Z",
            "updated_at": "2023-03-22T11:50:00Z"
        },
        {
            "customer_id": 35,
            "name": "Mia Taylor",
            "email": "mia.taylor@example.com",
            "country": "US",
            "created_at": "2023-03-25T16:15:00Z",
            "updated_at": "2023-03-25T16:15:00Z"
        },
        {
            "customer_id": 36,
            "name": "Noah Miller",
            "email": "noah.miller@example.com",
            "country": "US",
            "created_at": "2023-03-28T09:30:00Z",
            "updated_at": "2023-03-28T09:30:00Z"
        },
        {
            "customer_id": 37,
            "name": "Isabella Garcia",
            "email": "isabella.garcia@example.com",
            "country": "US",
            "created_at": "2023-03-31T13:45:00Z",
            "updated_at": "2023-03-31T13:45:00Z"
        },
        {
            "customer_id": 38,
            "name": "William Davis",
            "email": "william.davis@example.com",
            "country": "CA",
            "created_at": "2023-04-03T15:00:00Z",
            "updated_at": "2023-04-03T15:00:00Z"
        },
        {
            "customer_id": 39,
            "name": "Olivia Tremblay",
            "email": "olivia.tremblay@example.com",
            "country": "CA",
            "created_at": "2023-04-06T18:10:00Z",
            "updated_at": "2023-04-06T18:10:00Z"
        },
        {
            "customer_id": 40,
            "name": "Mateo Fernandez",
            "email": "mateo.fernandez@example.com",
            "country": "MX",
            "created_at": "2023-04-09T10:30:00Z",
            "updated_at": "2023-04-09T10:30:00Z"
        },
        {
            "customer_id": 41,
            "name": "Sofia Lopez",
            "email": "sofia.lopez@example.com",
            "country": "MX",
            "created_at": "2023-04-12T14:20:00Z",
            "updated_at": "2023-04-12T14:20:00Z"
        },
        {
            "customer_id": 42,
            "name": "Astrid Lindgren",
            "email": "astrid.lindgren@example.com",
            "country": "SE",
            "created_at": "2023-04-15T11:45:00Z",
            "updated_at": "2023-04-15T11:45:00Z"
        },
        {
            "customer_id": 43,
            "name": "Erik Johansson",
            "email": "erik.johansson@example.com",
            "country": "SE",
            "created_at": "2023-04-18T16:00:00Z",
            "updated_at": "2023-04-18T16:00:00Z"
        },
        {
            "customer_id": 44,
            "name": "Daniel Kim",
            "email": "daniel.kim@example.com",
            "country": "KR",
            "created_at": "2023-04-21T09:15:00Z",
            "updated_at": "2023-04-21T09:15:00Z"
        },
        {
            "customer_id": 45,
            "name": "Min-ji Park",
            "email": "minji.park@example.com",
            "country": "KR",
            "created_at": "2023-04-24T13:50:00Z",
            "updated_at": "2023-04-24T13:50:00Z"
        },
        {
            "customer_id": 46,
            "name": "Jack Thompson",
            "email": "jack.thompson@example.com",
            "country": "AU",
            "created_at": "2023-04-27T08:25:00Z",
            "updated_at": "2023-04-27T08:25:00Z"
        },
        {
            "customer_id": 47,
            "name": "Chloe Wilson",
            "email": "chloe.wilson@example.com",
            "country": "AU",
            "created_at": "2023-04-30T15:40:00Z",
            "updated_at": "2023-04-30T15:40:00Z"
        },
        {
            "customer_id": 48,
            "name": "Miguel Pereira",
            "email": "miguel.pereira@example.com",
            "country": "PT",
            "created_at": "2023-05-03T10:10:00Z",
            "updated_at": "2023-05-03T10:10:00Z"
        },
        {
            "customer_id": 49,
            "name": "Ines Sousa",
            "email": "ines.sousa@example.com",
            "country": "PT",
            "created_at": "2023-05-06T14:35:00Z",
            "updated_at": "2023-05-06T14:35:00Z"
        },
        {
            "customer_id": 50,
            "name": "Rui Rodrigues",
            "email": "rui.rodrigues@example.com",
            "country": "PT",
            "created_at": "2023-05-09T17:20:00Z",
            "updated_at": "2023-05-09T17:20:00Z"
        }
    ]
    return users[offset:offset + limit]


@app.get("/products")
def get_products(limit: int = 5, offset: int = 0):
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
        },
        {
            "product_id": 6,
            "name": "Wireless Bluetooth Headphones",
            "category": "Electronics",
            "price": 59.99,
            "stock": 80,
            "created_at": "2023-01-05T00:00:00Z",
            "updated_at": "2023-01-05T00:00:00Z"
        },
        {
            "product_id": 7,
            "name": "Mechanical Gaming Keyboard",
            "category": "Electronics",
            "price": 89.99,
            "stock": 45,
            "created_at": "2023-01-06T00:00:00Z",
            "updated_at": "2023-01-06T00:00:00Z"
        },
        {
            "product_id": 8,
            "name": "Ergonomic Mouse",
            "category": "Electronics",
            "price": 24.99,
            "stock": 120,
            "created_at": "2023-01-07T00:00:00Z",
            "updated_at": "2023-01-07T00:00:00Z"
        },
        {
            "product_id": 9,
            "name": "27-inch 4K Monitor",
            "category": "Electronics",
            "price": 299.99,
            "stock": 25,
            "created_at": "2023-01-08T00:00:00Z",
            "updated_at": "2023-01-08T00:00:00Z"
        },
        {
            "product_id": 10,
            "name": "USB-C Fast Charger",
            "category": "Electronics",
            "price": 15.99,
            "stock": 150,
            "created_at": "2023-01-09T00:00:00Z",
            "updated_at": "2023-01-09T00:00:00Z"
        },
        {
            "product_id": 11,
            "name": "Cotton Crewneck T-Shirt",
            "category": "Clothing",
            "price": 18.50,
            "stock": 200,
            "created_at": "2023-01-10T00:00:00Z",
            "updated_at": "2023-01-10T00:00:00Z"
        },
        {
            "product_id": 12,
            "name": "Slim Fit Denim Jeans",
            "category": "Clothing",
            "price": 49.99,
            "stock": 90,
            "created_at": "2023-01-11T00:00:00Z",
            "updated_at": "2023-01-11T00:00:00Z"
        },
        {
            "product_id": 13,
            "name": "Waterproof Winter Jacket",
            "category": "Clothing",
            "price": 119.99,
            "stock": 40,
            "created_at": "2023-01-12T00:00:00Z",
            "updated_at": "2023-01-12T00:00:00Z"
        },
        {
            "product_id": 14,
            "name": "Breathable Running Shoes",
            "category": "Sports",
            "price": 79.99,
            "stock": 60,
            "created_at": "2023-01-13T00:00:00Z",
            "updated_at": "2023-01-13T00:00:00Z"
        },
        {
            "product_id": 15,
            "name": "Classic Leather Belt",
            "category": "Accessories",
            "price": 22.00,
            "stock": 110,
            "created_at": "2023-01-14T00:00:00Z",
            "updated_at": "2023-01-14T00:00:00Z"
        },
        {
            "product_id": 16,
            "name": "Stainless Steel Water Bottle 750ml",
            "category": "Sports",
            "price": 16.99,
            "stock": 130,
            "created_at": "2023-01-15T00:00:00Z",
            "updated_at": "2023-01-15T00:00:00Z"
        },
        {
            "product_id": 17,
            "name": "Yoga Mat Non-Slip",
            "category": "Sports",
            "price": 25.50,
            "stock": 70,
            "created_at": "2023-01-16T00:00:00Z",
            "updated_at": "2023-01-16T00:00:00Z"
        },
        {
            "product_id": 18,
            "name": "Ceramic Coffee Mug Set",
            "category": "Home & Kitchen",
            "price": 21.99,
            "stock": 85,
            "created_at": "2023-01-17T00:00:00Z",
            "updated_at": "2023-01-17T00:00:00Z"
        },
        {
            "product_id": 19,
            "name": "French Press Coffee Maker",
            "category": "Home & Kitchen",
            "price": 32.50,
            "stock": 55,
            "created_at": "2023-01-18T00:00:00Z",
            "updated_at": "2023-01-18T00:00:00Z"
        },
        {
            "product_id": 20,
            "name": "Non-Stick Frying Pan 28cm",
            "category": "Home & Kitchen",
            "price": 34.99,
            "stock": 65,
            "created_at": "2023-01-19T00:00:00Z",
            "updated_at": "2023-01-19T00:00:00Z"
        },
        {
            "product_id": 21,
            "name": "Memory Foam Pillow",
            "category": "Home & Kitchen",
            "price": 29.99,
            "stock": 95,
            "created_at": "2023-01-20T00:00:00Z",
            "updated_at": "2023-01-20T00:00:00Z"
        },
        {
            "product_id": 22,
            "name": "LED Desk Lamp with Dimmer",
            "category": "Home & Kitchen",
            "price": 27.99,
            "stock": 80,
            "created_at": "2023-01-21T00:00:00Z",
            "updated_at": "2023-01-21T00:00:00Z"
        },
        {
            "product_id": 23,
            "name": "Hardcover Ruled Notebook",
            "category": "Stationery",
            "price": 8.99,
            "stock": 250,
            "created_at": "2023-01-22T00:00:00Z",
            "updated_at": "2023-01-22T00:00:00Z"
        },
        {
            "product_id": 24,
            "name": "Gel Pen Pack (10 pcs)",
            "category": "Stationery",
            "price": 6.49,
            "stock": 300,
            "created_at": "2023-01-23T00:00:00Z",
            "updated_at": "2023-01-23T00:00:00Z"
        },
        {
            "product_id": 25,
            "name": "Noise-Cancelling Earbuds",
            "category": "Electronics",
            "price": 49.99,
            "stock": 110,
            "created_at": "2023-01-24T00:00:00Z",
            "updated_at": "2023-01-24T00:00:00Z"
        },
        {
            "product_id": 26,
            "name": "Canvas Backpack 20L",
            "category": "Accessories",
            "price": 45.00,
            "stock": 75,
            "created_at": "2023-01-25T00:00:00Z",
            "updated_at": "2023-01-25T00:00:00Z"
        },
        {
            "product_id": 27,
            "name": "Polarized Sunglasses",
            "category": "Accessories",
            "price": 35.00,
            "stock": 90,
            "created_at": "2023-01-26T00:00:00Z",
            "updated_at": "2023-01-26T00:00:00Z"
        },
        {
            "product_id": 28,
            "name": "Portable Bluetooth Speaker",
            "category": "Electronics",
            "price": 39.99,
            "stock": 65,
            "created_at": "2023-01-27T00:00:00Z",
            "updated_at": "2023-01-27T00:00:00Z"
        },
        {
            "product_id": 29,
            "name": "Stainless Steel Kitchen Knife Set",
            "category": "Home & Kitchen",
            "price": 64.99,
            "stock": 40,
            "created_at": "2023-01-28T00:00:00Z",
            "updated_at": "2023-01-28T00:00:00Z"
        },
        {
            "product_id": 30,
            "name": "Smart Fitness Tracker Band",
            "category": "Electronics",
            "price": 44.99,
            "stock": 85,
            "created_at": "2023-01-29T00:00:00Z",
            "updated_at": "2023-01-29T00:00:00Z"
        }
    ]
    return products[offset:offset + limit]


@app.get("/orders")
def get_orders(limit: int = 5, offset: int = 0):
    orders = [
        {
            "order_id": 1,
            "customer_id": 1,
            "order_date": "2023-01-01T00:00:00Z",
            "status": "shipped",
            "total_amount": 69.97,
            "updated_at": "2023-01-01T00:00:00Z",
            "items": [
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
            "items": [
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
            "items": [
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
            "items": []
        },
        {
            "order_id": 5,
            "customer_id": 2,
            "order_date": "2023-01-05T00:00:00Z",
            "status": "shipped",
            "total_amount": 79.98,
            "updated_at": "2023-01-05T00:00:00Z",
            "items": [
                {
                    "product_id": 5,
                    "quantity": 2,
                    "unit_price": 39.99
                }
            ]
        },
        {
            "order_id": 6,
            "customer_id": 41,
            "order_date": "2023-01-06T15:42:00Z",
            "status": "cancelled",
            "total_amount": 0.00,
            "updated_at": "2023-01-06T15:42:00Z",
            "items": []
        },
        {
            "order_id": 7,
            "customer_id": 8,
            "order_date": "2023-01-10T20:49:00Z",
            "status": "pending",
            "total_amount": 72.95,
            "updated_at": "2023-01-10T20:49:00Z",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 3,
                    "unit_price": 19.99
                },
                {
                    "product_id": 24,
                    "quantity": 2,
                    "unit_price": 6.49
                }
            ]
        },
        {
            "order_id": 8,
            "customer_id": 15,
            "order_date": "2023-01-12T13:56:00Z",
            "status": "delivered",
            "total_amount": 80.94,
            "updated_at": "2023-01-12T13:56:00Z",
            "items": [
                {
                    "product_id": 5,
                    "quantity": 1,
                    "unit_price": 39.99
                },
                {
                    "product_id": 24,
                    "quantity": 4,
                    "unit_price": 6.49
                },
                {
                    "product_id": 4,
                    "quantity": 1,
                    "unit_price": 14.99
                }
            ]
        },
        {
            "order_id": 9,
            "customer_id": 2,
            "order_date": "2023-01-16T18:03:00Z",
            "status": "delivered",
            "total_amount": 19.98,
            "updated_at": "2023-01-16T18:03:00Z",
            "items": [
                {
                    "product_id": 3,
                    "quantity": 2,
                    "unit_price": 9.99
                }
            ]
        },
        {
            "order_id": 10,
            "customer_id": 15,
            "order_date": "2023-01-18T11:10:00Z",
            "status": "delivered",
            "total_amount": 95.48,
            "updated_at": "2023-01-18T11:10:00Z",
            "items": [
                {
                    "product_id": 17,
                    "quantity": 1,
                    "unit_price": 25.50
                },
                {
                    "product_id": 20,
                    "quantity": 2,
                    "unit_price": 34.99
                }
            ]
        },
        {
            "order_id": 11,
            "customer_id": 46,
            "order_date": "2023-01-22T16:17:00Z",
            "status": "shipped",
            "total_amount": 225.90,
            "updated_at": "2023-01-22T16:17:00Z",
            "items": [
                {
                    "product_id": 21,
                    "quantity": 4,
                    "unit_price": 29.99
                },
                {
                    "product_id": 23,
                    "quantity": 2,
                    "unit_price": 8.99
                },
                {
                    "product_id": 18,
                    "quantity": 4,
                    "unit_price": 21.99
                }
            ]
        },
        {
            "order_id": 12,
            "customer_id": 38,
            "order_date": "2023-01-24T09:24:00Z",
            "status": "shipped",
            "total_amount": 299.99,
            "updated_at": "2023-01-24T09:24:00Z",
            "items": [
                {
                    "product_id": 9,
                    "quantity": 1,
                    "unit_price": 299.99
                }
            ]
        },
        {
            "order_id": 13,
            "customer_id": 49,
            "order_date": "2023-01-28T14:31:00Z",
            "status": "processing",
            "total_amount": 359.97,
            "updated_at": "2023-01-28T14:31:00Z",
            "items": [
                {
                    "product_id": 26,
                    "quantity": 4,
                    "unit_price": 45.00
                },
                {
                    "product_id": 6,
                    "quantity": 3,
                    "unit_price": 59.99
                }
            ]
        },
        {
            "order_id": 14,
            "customer_id": 18,
            "order_date": "2023-01-30T19:38:00Z",
            "status": "cancelled",
            "total_amount": 259.95,
            "updated_at": "2023-01-30T19:38:00Z",
            "items": [
                {
                    "product_id": 5,
                    "quantity": 3,
                    "unit_price": 39.99
                },
                {
                    "product_id": 7,
                    "quantity": 1,
                    "unit_price": 89.99
                },
                {
                    "product_id": 25,
                    "quantity": 1,
                    "unit_price": 49.99
                }
            ]
        },
        {
            "order_id": 15,
            "customer_id": 25,
            "order_date": "2023-02-03T12:45:00Z",
            "status": "pending",
            "total_amount": 44.97,
            "updated_at": "2023-02-03T12:45:00Z",
            "items": [
                {
                    "product_id": 4,
                    "quantity": 3,
                    "unit_price": 14.99
                }
            ]
        },
        {
            "order_id": 16,
            "customer_id": 23,
            "order_date": "2023-02-05T17:52:00Z",
            "status": "delivered",
            "total_amount": 1234.95,
            "updated_at": "2023-02-05T17:52:00Z",
            "items": [
                {
                    "product_id": 20,
                    "quantity": 1,
                    "unit_price": 34.99
                },
                {
                    "product_id": 9,
                    "quantity": 4,
                    "unit_price": 299.99
                }
            ]
        },
        {
            "order_id": 17,
            "customer_id": 35,
            "order_date": "2023-02-09T10:59:00Z",
            "status": "delivered",
            "total_amount": 509.93,
            "updated_at": "2023-02-09T10:59:00Z",
            "items": [
                {
                    "product_id": 4,
                    "quantity": 1,
                    "unit_price": 14.99
                },
                {
                    "product_id": 30,
                    "quantity": 3,
                    "unit_price": 44.99
                },
                {
                    "product_id": 13,
                    "quantity": 3,
                    "unit_price": 119.99
                }
            ]
        },
        {
            "order_id": 18,
            "customer_id": 37,
            "order_date": "2023-02-11T15:06:00Z",
            "status": "delivered",
            "total_amount": 89.99,
            "updated_at": "2023-02-11T15:06:00Z",
            "items": [
                {
                    "product_id": 7,
                    "quantity": 1,
                    "unit_price": 89.99
                }
            ]
        },
        {
            "order_id": 19,
            "customer_id": 3,
            "order_date": "2023-02-15T20:13:00Z",
            "status": "shipped",
            "total_amount": 108.96,
            "updated_at": "2023-02-15T20:13:00Z",
            "items": [
                {
                    "product_id": 22,
                    "quantity": 3,
                    "unit_price": 27.99
                },
                {
                    "product_id": 8,
                    "quantity": 1,
                    "unit_price": 24.99
                }
            ]
        },
        {
            "order_id": 20,
            "customer_id": 15,
            "order_date": "2023-02-17T13:20:00Z",
            "status": "shipped",
            "total_amount": 539.90,
            "updated_at": "2023-02-17T13:20:00Z",
            "items": [
                {
                    "product_id": 28,
                    "quantity": 3,
                    "unit_price": 39.99
                },
                {
                    "product_id": 4,
                    "quantity": 4,
                    "unit_price": 14.99
                },
                {
                    "product_id": 13,
                    "quantity": 3,
                    "unit_price": 119.99
                }
            ]
        },
        {
            "order_id": 21,
            "customer_id": 11,
            "order_date": "2023-02-21T18:27:00Z",
            "status": "processing",
            "total_amount": 149.97,
            "updated_at": "2023-02-21T18:27:00Z",
            "items": [
                {
                    "product_id": 12,
                    "quantity": 3,
                    "unit_price": 49.99
                }
            ]
        },
        {
            "order_id": 22,
            "customer_id": 14,
            "order_date": "2023-02-23T11:34:00Z",
            "status": "cancelled",
            "total_amount": 627.97,
            "updated_at": "2023-02-23T11:34:00Z",
            "items": [
                {
                    "product_id": 22,
                    "quantity": 1,
                    "unit_price": 27.99
                },
                {
                    "product_id": 9,
                    "quantity": 2,
                    "unit_price": 299.99
                }
            ]
        },
        {
            "order_id": 23,
            "customer_id": 35,
            "order_date": "2023-02-27T16:41:00Z",
            "status": "pending",
            "total_amount": 305.89,
            "updated_at": "2023-02-27T16:41:00Z",
            "items": [
                {
                    "product_id": 24,
                    "quantity": 4,
                    "unit_price": 6.49
                },
                {
                    "product_id": 8,
                    "quantity": 4,
                    "unit_price": 24.99
                },
                {
                    "product_id": 6,
                    "quantity": 3,
                    "unit_price": 59.99
                }
            ]
        },
        {
            "order_id": 24,
            "customer_id": 41,
            "order_date": "2023-03-01T09:48:00Z",
            "status": "delivered",
            "total_amount": 17.98,
            "updated_at": "2023-03-01T09:48:00Z",
            "items": [
                {
                    "product_id": 23,
                    "quantity": 2,
                    "unit_price": 8.99
                }
            ]
        },
        {
            "order_id": 25,
            "customer_id": 44,
            "order_date": "2023-03-05T14:55:00Z",
            "status": "delivered",
            "total_amount": 88.50,
            "updated_at": "2023-03-05T14:55:00Z",
            "items": [
                {
                    "product_id": 11,
                    "quantity": 1,
                    "unit_price": 18.50
                },
                {
                    "product_id": 27,
                    "quantity": 2,
                    "unit_price": 35.00
                }
            ]
        },
        {
            "order_id": 26,
            "customer_id": 3,
            "order_date": "2023-03-07T19:02:00Z",
            "status": "delivered",
            "total_amount": 393.48,
            "updated_at": "2023-03-07T19:02:00Z",
            "items": [
                {
                    "product_id": 26,
                    "quantity": 3,
                    "unit_price": 45.00
                },
                {
                    "product_id": 11,
                    "quantity": 1,
                    "unit_price": 18.50
                },
                {
                    "product_id": 13,
                    "quantity": 2,
                    "unit_price": 119.99
                }
            ]
        },
        {
            "order_id": 27,
            "customer_id": 37,
            "order_date": "2023-03-11T12:09:00Z",
            "status": "shipped",
            "total_amount": 194.97,
            "updated_at": "2023-03-11T12:09:00Z",
            "items": [
                {
                    "product_id": 29,
                    "quantity": 3,
                    "unit_price": 64.99
                }
            ]
        },
        {
            "order_id": 28,
            "customer_id": 14,
            "order_date": "2023-03-13T17:16:00Z",
            "status": "shipped",
            "total_amount": 187.92,
            "updated_at": "2023-03-13T17:16:00Z",
            "items": [
                {
                    "product_id": 21,
                    "quantity": 4,
                    "unit_price": 29.99
                },
                {
                    "product_id": 16,
                    "quantity": 4,
                    "unit_price": 16.99
                }
            ]
        },
        {
            "order_id": 29,
            "customer_id": 10,
            "order_date": "2023-03-17T10:23:00Z",
            "status": "processing",
            "total_amount": 1159.89,
            "updated_at": "2023-03-17T10:23:00Z",
            "items": [
                {
                    "product_id": 9,
                    "quantity": 3,
                    "unit_price": 299.99
                },
                {
                    "product_id": 5,
                    "quantity": 4,
                    "unit_price": 39.99
                },
                {
                    "product_id": 8,
                    "quantity": 4,
                    "unit_price": 24.99
                }
            ]
        },
        {
            "order_id": 30,
            "customer_id": 24,
            "order_date": "2023-03-19T15:30:00Z",
            "status": "cancelled",
            "total_amount": 0.00,
            "updated_at": "2023-03-19T15:30:00Z",
            "items": []
        },
        {
            "order_id": 31,
            "customer_id": 15,
            "order_date": "2023-03-23T20:37:00Z",
            "status": "pending",
            "total_amount": 185.46,
            "updated_at": "2023-03-23T20:37:00Z",
            "items": [
                {
                    "product_id": 5,
                    "quantity": 4,
                    "unit_price": 39.99
                },
                {
                    "product_id": 17,
                    "quantity": 1,
                    "unit_price": 25.50
                }
            ]
        },
        {
            "order_id": 32,
            "customer_id": 49,
            "order_date": "2023-03-25T13:44:00Z",
            "status": "delivered",
            "total_amount": 199.92,
            "updated_at": "2023-03-25T13:44:00Z",
            "items": [
                {
                    "product_id": 2,
                    "quantity": 2,
                    "unit_price": 29.99
                },
                {
                    "product_id": 28,
                    "quantity": 2,
                    "unit_price": 39.99
                },
                {
                    "product_id": 4,
                    "quantity": 4,
                    "unit_price": 14.99
                }
            ]
        },
        {
            "order_id": 33,
            "customer_id": 39,
            "order_date": "2023-03-29T18:51:00Z",
            "status": "delivered",
            "total_amount": 39.96,
            "updated_at": "2023-03-29T18:51:00Z",
            "items": [
                {
                    "product_id": 3,
                    "quantity": 4,
                    "unit_price": 9.99
                }
            ]
        },
        {
            "order_id": 34,
            "customer_id": 25,
            "order_date": "2023-03-31T11:58:00Z",
            "status": "delivered",
            "total_amount": 126.97,
            "updated_at": "2023-03-31T11:58:00Z",
            "items": [
                {
                    "product_id": 20,
                    "quantity": 3,
                    "unit_price": 34.99
                },
                {
                    "product_id": 15,
                    "quantity": 1,
                    "unit_price": 22.00
                }
            ]
        },
        {
            "order_id": 35,
            "customer_id": 44,
            "order_date": "2023-04-04T16:05:00Z",
            "status": "shipped",
            "total_amount": 92.43,
            "updated_at": "2023-04-04T16:05:00Z",
            "items": [
                {
                    "product_id": 24,
                    "quantity": 3,
                    "unit_price": 6.49
                },
                {
                    "product_id": 4,
                    "quantity": 3,
                    "unit_price": 14.99
                },
                {
                    "product_id": 22,
                    "quantity": 1,
                    "unit_price": 27.99
                }
            ]
        },
        {
            "order_id": 36,
            "customer_id": 19,
            "order_date": "2023-04-06T09:12:00Z",
            "status": "shipped",
            "total_amount": 159.98,
            "updated_at": "2023-04-06T09:12:00Z",
            "items": [
                {
                    "product_id": 14,
                    "quantity": 2,
                    "unit_price": 79.99
                }
            ]
        },
        {
            "order_id": 37,
            "customer_id": 30,
            "order_date": "2023-04-10T14:19:00Z",
            "status": "processing",
            "total_amount": 72.95,
            "updated_at": "2023-04-10T14:19:00Z",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 3,
                    "unit_price": 19.99
                },
                {
                    "product_id": 24,
                    "quantity": 2,
                    "unit_price": 6.49
                }
            ]
        },
        {
            "order_id": 38,
            "customer_id": 33,
            "order_date": "2023-04-12T19:26:00Z",
            "status": "cancelled",
            "total_amount": 244.93,
            "updated_at": "2023-04-12T19:26:00Z",
            "items": [
                {
                    "product_id": 30,
                    "quantity": 3,
                    "unit_price": 44.99
                },
                {
                    "product_id": 4,
                    "quantity": 2,
                    "unit_price": 14.99
                },
                {
                    "product_id": 28,
                    "quantity": 2,
                    "unit_price": 39.99
                }
            ]
        },
        {
            "order_id": 39,
            "customer_id": 24,
            "order_date": "2023-04-16T12:33:00Z",
            "status": "pending",
            "total_amount": 99.98,
            "updated_at": "2023-04-16T12:33:00Z",
            "items": [
                {
                    "product_id": 25,
                    "quantity": 2,
                    "unit_price": 49.99
                }
            ]
        },
        {
            "order_id": 40,
            "customer_id": 35,
            "order_date": "2023-04-18T17:40:00Z",
            "status": "delivered",
            "total_amount": 184.96,
            "updated_at": "2023-04-18T17:40:00Z",
            "items": [
                {
                    "product_id": 25,
                    "quantity": 1,
                    "unit_price": 49.99
                },
                {
                    "product_id": 30,
                    "quantity": 3,
                    "unit_price": 44.99
                }
            ]
        },
        {
            "order_id": 41,
            "customer_id": 32,
            "order_date": "2023-04-22T10:47:00Z",
            "status": "delivered",
            "total_amount": 194.92,
            "updated_at": "2023-04-22T10:47:00Z",
            "items": [
                {
                    "product_id": 1,
                    "quantity": 3,
                    "unit_price": 19.99
                },
                {
                    "product_id": 4,
                    "quantity": 3,
                    "unit_price": 14.99
                },
                {
                    "product_id": 30,
                    "quantity": 2,
                    "unit_price": 44.99
                }
            ]
        },
        {
            "order_id": 42,
            "customer_id": 4,
            "order_date": "2023-04-24T15:54:00Z",
            "status": "delivered",
            "total_amount": 24.99,
            "updated_at": "2023-04-24T15:54:00Z",
            "items": [
                {
                    "product_id": 8,
                    "quantity": 1,
                    "unit_price": 24.99
                }
            ]
        },
        {
            "order_id": 43,
            "customer_id": 6,
            "order_date": "2023-04-28T20:01:00Z",
            "status": "shipped",
            "total_amount": 40.47,
            "updated_at": "2023-04-28T20:01:00Z",
            "items": [
                {
                    "product_id": 24,
                    "quantity": 1,
                    "unit_price": 6.49
                },
                {
                    "product_id": 16,
                    "quantity": 2,
                    "unit_price": 16.99
                }
            ]
        },
        {
            "order_id": 44,
            "customer_id": 9,
            "order_date": "2023-04-30T13:08:00Z",
            "status": "shipped",
            "total_amount": 194.91,
            "updated_at": "2023-04-30T13:08:00Z",
            "items": [
                {
                    "product_id": 22,
                    "quantity": 2,
                    "unit_price": 27.99
                },
                {
                    "product_id": 16,
                    "quantity": 3,
                    "unit_price": 16.99
                },
                {
                    "product_id": 18,
                    "quantity": 4,
                    "unit_price": 21.99
                }
            ]
        },
        {
            "order_id": 45,
            "customer_id": 14,
            "order_date": "2023-05-04T18:15:00Z",
            "status": "processing",
            "total_amount": 89.98,
            "updated_at": "2023-05-04T18:15:00Z",
            "items": [
                {
                    "product_id": 30,
                    "quantity": 2,
                    "unit_price": 44.99
                }
            ]
        },
        {
            "order_id": 46,
            "customer_id": 46,
            "order_date": "2023-05-06T11:22:00Z",
            "status": "cancelled",
            "total_amount": 527.93,
            "updated_at": "2023-05-06T11:22:00Z",
            "items": [
                {
                    "product_id": 10,
                    "quantity": 3,
                    "unit_price": 15.99
                },
                {
                    "product_id": 13,
                    "quantity": 4,
                    "unit_price": 119.99
                }
            ]
        },
        {
            "order_id": 47,
            "customer_id": 34,
            "order_date": "2023-05-10T16:29:00Z",
            "status": "pending",
            "total_amount": 133.96,
            "updated_at": "2023-05-10T16:29:00Z",
            "items": [
                {
                    "product_id": 15,
                    "quantity": 2,
                    "unit_price": 22.00
                },
                {
                    "product_id": 4,
                    "quantity": 1,
                    "unit_price": 14.99
                },
                {
                    "product_id": 8,
                    "quantity": 3,
                    "unit_price": 24.99
                }
            ]
        },
        {
            "order_id": 48,
            "customer_id": 2,
            "order_date": "2023-05-12T09:36:00Z",
            "status": "delivered",
            "total_amount": 65.00,
            "updated_at": "2023-05-12T09:36:00Z",
            "items": [
                {
                    "product_id": 19,
                    "quantity": 2,
                    "unit_price": 32.50
                }
            ]
        },
        {
            "order_id": 49,
            "customer_id": 38,
            "order_date": "2023-05-16T14:43:00Z",
            "status": "delivered",
            "total_amount": 44.98,
            "updated_at": "2023-05-16T14:43:00Z",
            "items": [
                {
                    "product_id": 8,
                    "quantity": 1,
                    "unit_price": 24.99
                },
                {
                    "product_id": 1,
                    "quantity": 1,
                    "unit_price": 19.99
                }
            ]
        },
        {
            "order_id": 50,
            "customer_id": 15,
            "order_date": "2023-05-18T19:50:00Z",
            "status": "delivered",
            "total_amount": 154.94,
            "updated_at": "2023-05-18T19:50:00Z",
            "items": [
                {
                    "product_id": 3,
                    "quantity": 3,
                    "unit_price": 9.99
                },
                {
                    "product_id": 29,
                    "quantity": 1,
                    "unit_price": 64.99
                },
                {
                    "product_id": 2,
                    "quantity": 2,
                    "unit_price": 29.99
                }
            ]
        }
    ]
    return orders[offset:offset + limit]


@app.get("/payments")
def get_payments(limit: int = 5, offset: int = 0):
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
        },
        {
            "payment_id": 6,
            "order_id": 6,
            "payment_method": "credit_card",
            "amount": 0.00,
            "status": "failed",
            "payment_date": None,
            "updated_at": None
        },
        {
            "payment_id": 7,
            "order_id": 7,
            "payment_method": "paypal",
            "amount": 72.95,
            "status": "pending",
            "payment_date": "2023-01-10T20:49:00Z",
            "updated_at": "2023-01-10T20:49:00Z"
        },
        {
            "payment_id": 8,
            "order_id": 8,
            "payment_method": "bank_transfer",
            "amount": 80.94,
            "status": "completed",
            "payment_date": "2023-01-12T13:56:00Z",
            "updated_at": "2023-01-12T13:56:00Z"
        },
        {
            "payment_id": 9,
            "order_id": 9,
            "payment_method": "apple_pay",
            "amount": 19.98,
            "status": "completed",
            "payment_date": "2023-01-16T18:03:00Z",
            "updated_at": "2023-01-16T18:03:00Z"
        },
        {
            "payment_id": 10,
            "order_id": 10,
            "payment_method": "mbway",
            "amount": 95.48,
            "status": "completed",
            "payment_date": "2023-01-18T11:10:00Z",
            "updated_at": "2023-01-18T11:10:00Z"
        },
        {
            "payment_id": 11,
            "order_id": 11,
            "payment_method": "debit_card",
            "amount": 225.90,
            "status": "completed",
            "payment_date": "2023-01-22T16:17:00Z",
            "updated_at": "2023-01-22T16:17:00Z"
        },
        {
            "payment_id": 12,
            "order_id": 12,
            "payment_method": "credit_card",
            "amount": 299.99,
            "status": "completed",
            "payment_date": "2023-01-24T09:24:00Z",
            "updated_at": "2023-01-24T09:24:00Z"
        },
        {
            "payment_id": 13,
            "order_id": 13,
            "payment_method": "paypal",
            "amount": 359.97,
            "status": "pending",
            "payment_date": "2023-01-28T14:31:00Z",
            "updated_at": "2023-01-28T14:31:00Z"
        },
        {
            "payment_id": 14,
            "order_id": 14,
            "payment_method": "bank_transfer",
            "amount": 0.00,
            "status": "failed",
            "payment_date": None,
            "updated_at": None
        },
        {
            "payment_id": 15,
            "order_id": 15,
            "payment_method": "apple_pay",
            "amount": 44.97,
            "status": "pending",
            "payment_date": "2023-02-03T12:45:00Z",
            "updated_at": "2023-02-03T12:45:00Z"
        },
        {
            "payment_id": 16,
            "order_id": 16,
            "payment_method": "mbway",
            "amount": 1234.95,
            "status": "completed",
            "payment_date": "2023-02-05T17:52:00Z",
            "updated_at": "2023-02-05T17:52:00Z"
        },
        {
            "payment_id": 17,
            "order_id": 17,
            "payment_method": "debit_card",
            "amount": 509.93,
            "status": "completed",
            "payment_date": "2023-02-09T10:59:00Z",
            "updated_at": "2023-02-09T10:59:00Z"
        },
        {
            "payment_id": 18,
            "order_id": 18,
            "payment_method": "credit_card",
            "amount": 89.99,
            "status": "completed",
            "payment_date": "2023-02-11T15:06:00Z",
            "updated_at": "2023-02-11T15:06:00Z"
        },
        {
            "payment_id": 19,
            "order_id": 19,
            "payment_method": "paypal",
            "amount": 108.96,
            "status": "completed",
            "payment_date": "2023-02-15T20:13:00Z",
            "updated_at": "2023-02-15T20:13:00Z"
        },
        {
            "payment_id": 20,
            "order_id": 20,
            "payment_method": "bank_transfer",
            "amount": 539.90,
            "status": "completed",
            "payment_date": "2023-02-17T13:20:00Z",
            "updated_at": "2023-02-17T13:20:00Z"
        },
        {
            "payment_id": 21,
            "order_id": 21,
            "payment_method": "apple_pay",
            "amount": 149.97,
            "status": "pending",
            "payment_date": "2023-02-21T18:27:00Z",
            "updated_at": "2023-02-21T18:27:00Z"
        },
        {
            "payment_id": 22,
            "order_id": 22,
            "payment_method": "mbway",
            "amount": 0.00,
            "status": "failed",
            "payment_date": None,
            "updated_at": None
        },
        {
            "payment_id": 23,
            "order_id": 23,
            "payment_method": "debit_card",
            "amount": 305.89,
            "status": "pending",
            "payment_date": "2023-02-27T16:41:00Z",
            "updated_at": "2023-02-27T16:41:00Z"
        },
        {
            "payment_id": 24,
            "order_id": 24,
            "payment_method": "credit_card",
            "amount": 17.98,
            "status": "completed",
            "payment_date": "2023-03-01T09:48:00Z",
            "updated_at": "2023-03-01T09:48:00Z"
        },
        {
            "payment_id": 25,
            "order_id": 25,
            "payment_method": "paypal",
            "amount": 88.50,
            "status": "completed",
            "payment_date": "2023-03-05T14:55:00Z",
            "updated_at": "2023-03-05T14:55:00Z"
        },
        {
            "payment_id": 26,
            "order_id": 26,
            "payment_method": "bank_transfer",
            "amount": 393.48,
            "status": "completed",
            "payment_date": "2023-03-07T19:02:00Z",
            "updated_at": "2023-03-07T19:02:00Z"
        },
        {
            "payment_id": 27,
            "order_id": 27,
            "payment_method": "apple_pay",
            "amount": 194.97,
            "status": "completed",
            "payment_date": "2023-03-11T12:09:00Z",
            "updated_at": "2023-03-11T12:09:00Z"
        },
        {
            "payment_id": 28,
            "order_id": 28,
            "payment_method": "mbway",
            "amount": 187.92,
            "status": "completed",
            "payment_date": "2023-03-13T17:16:00Z",
            "updated_at": "2023-03-13T17:16:00Z"
        },
        {
            "payment_id": 29,
            "order_id": 29,
            "payment_method": "debit_card",
            "amount": 1159.89,
            "status": "pending",
            "payment_date": "2023-03-17T10:23:00Z",
            "updated_at": "2023-03-17T10:23:00Z"
        },
        {
            "payment_id": 30,
            "order_id": 30,
            "payment_method": "credit_card",
            "amount": 0.00,
            "status": "failed",
            "payment_date": None,
            "updated_at": None
        },
        {
            "payment_id": 31,
            "order_id": 31,
            "payment_method": "paypal",
            "amount": 185.46,
            "status": "pending",
            "payment_date": "2023-03-23T20:37:00Z",
            "updated_at": "2023-03-23T20:37:00Z"
        },
        {
            "payment_id": 32,
            "order_id": 32,
            "payment_method": "bank_transfer",
            "amount": 199.92,
            "status": "completed",
            "payment_date": "2023-03-25T13:44:00Z",
            "updated_at": "2023-03-25T13:44:00Z"
        },
        {
            "payment_id": 33,
            "order_id": 33,
            "payment_method": "apple_pay",
            "amount": 39.96,
            "status": "completed",
            "payment_date": "2023-03-29T18:51:00Z",
            "updated_at": "2023-03-29T18:51:00Z"
        },
        {
            "payment_id": 34,
            "order_id": 34,
            "payment_method": "mbway",
            "amount": 126.97,
            "status": "completed",
            "payment_date": "2023-03-31T11:58:00Z",
            "updated_at": "2023-03-31T11:58:00Z"
        },
        {
            "payment_id": 35,
            "order_id": 35,
            "payment_method": "debit_card",
            "amount": 92.43,
            "status": "completed",
            "payment_date": "2023-04-04T16:05:00Z",
            "updated_at": "2023-04-04T16:05:00Z"
        },
        {
            "payment_id": 36,
            "order_id": 36,
            "payment_method": "credit_card",
            "amount": 159.98,
            "status": "completed",
            "payment_date": "2023-04-06T09:12:00Z",
            "updated_at": "2023-04-06T09:12:00Z"
        },
        {
            "payment_id": 37,
            "order_id": 37,
            "payment_method": "paypal",
            "amount": 72.95,
            "status": "pending",
            "payment_date": "2023-04-10T14:19:00Z",
            "updated_at": "2023-04-10T14:19:00Z"
        },
        {
            "payment_id": 38,
            "order_id": 38,
            "payment_method": "bank_transfer",
            "amount": 0.00,
            "status": "failed",
            "payment_date": None,
            "updated_at": None
        },
        {
            "payment_id": 39,
            "order_id": 39,
            "payment_method": "apple_pay",
            "amount": 99.98,
            "status": "pending",
            "payment_date": "2023-04-16T12:33:00Z",
            "updated_at": "2023-04-16T12:33:00Z"
        },
        {
            "payment_id": 40,
            "order_id": 40,
            "payment_method": "mbway",
            "amount": 184.96,
            "status": "completed",
            "payment_date": "2023-04-18T17:40:00Z",
            "updated_at": "2023-04-18T17:40:00Z"
        },
        {
            "payment_id": 41,
            "order_id": 41,
            "payment_method": "debit_card",
            "amount": 194.92,
            "status": "completed",
            "payment_date": "2023-04-22T10:47:00Z",
            "updated_at": "2023-04-22T10:47:00Z"
        },
        {
            "payment_id": 42,
            "order_id": 42,
            "payment_method": "credit_card",
            "amount": 24.99,
            "status": "completed",
            "payment_date": "2023-04-24T15:54:00Z",
            "updated_at": "2023-04-24T15:54:00Z"
        },
        {
            "payment_id": 43,
            "order_id": 43,
            "payment_method": "paypal",
            "amount": 40.47,
            "status": "completed",
            "payment_date": "2023-04-28T20:01:00Z",
            "updated_at": "2023-04-28T20:01:00Z"
        },
        {
            "payment_id": 44,
            "order_id": 44,
            "payment_method": "bank_transfer",
            "amount": 194.91,
            "status": "completed",
            "payment_date": "2023-04-30T13:08:00Z",
            "updated_at": "2023-04-30T13:08:00Z"
        },
        {
            "payment_id": 45,
            "order_id": 45,
            "payment_method": "apple_pay",
            "amount": 89.98,
            "status": "pending",
            "payment_date": "2023-05-04T18:15:00Z",
            "updated_at": "2023-05-04T18:15:00Z"
        },
        {
            "payment_id": 46,
            "order_id": 46,
            "payment_method": "mbway",
            "amount": 0.00,
            "status": "failed",
            "payment_date": None,
            "updated_at": None
        },
        {
            "payment_id": 47,
            "order_id": 47,
            "payment_method": "debit_card",
            "amount": 133.96,
            "status": "pending",
            "payment_date": "2023-05-10T16:29:00Z",
            "updated_at": "2023-05-10T16:29:00Z"
        },
        {
            "payment_id": 48,
            "order_id": 48,
            "payment_method": "credit_card",
            "amount": 65.00,
            "status": "completed",
            "payment_date": "2023-05-12T09:36:00Z",
            "updated_at": "2023-05-12T09:36:00Z"
        },
        {
            "payment_id": 49,
            "order_id": 49,
            "payment_method": "paypal",
            "amount": 44.98,
            "status": "completed",
            "payment_date": "2023-05-16T14:43:00Z",
            "updated_at": "2023-05-16T14:43:00Z"
        },
        {
            "payment_id": 50,
            "order_id": 50,
            "payment_method": "bank_transfer",
            "amount": 154.94,
            "status": "completed",
            "payment_date": "2023-05-18T19:50:00Z",
            "updated_at": "2023-05-18T19:50:00Z"
        }
    ]
    return payments[offset:offset + limit]
