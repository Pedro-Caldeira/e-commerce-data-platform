Insert into customers (
    customer_id,
    name,
    email,
    country,
    created_at,
    updated_at
)
Select
    customer_id,
    name,
    email,
    country,
    created_at,
    updated_at
From customers_staging
On Conflict (customer_id)
Do Update Set
    name = EXCLUDED.name,
    email = EXCLUDED.email,
    country = EXCLUDED.country,
    created_at = EXCLUDED.created_at,
    updated_at = EXCLUDED.updated_at;