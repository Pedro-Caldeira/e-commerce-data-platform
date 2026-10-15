INSERT INTO orders (
    order_id,
    customer_id,
    order_date,
    status,
    total_amount,
    updated_at
)
SELECT
    order_id,
    customer_id,
    order_date,
    status,
    total_amount,
    updated_at
FROM orders_staging
ON CONFLICT (order_id)
DO UPDATE SET
    customer_id = EXCLUDED.customer_id,
    order_date = EXCLUDED.order_date,
    status = EXCLUDED.status,
    total_amount = EXCLUDED.total_amount,
    updated_at = EXCLUDED.updated_at;