SELECT
    order_id,
    customer_id,
    order_date,
    LOWER(TRIM(status)) AS status,
    total_amount,
    updated_at
FROM {{ source('shopflow', 'orders') }}