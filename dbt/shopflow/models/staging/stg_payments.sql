SELECT
    payment_id,
    order_id,
    LOWER(TRIM(payment_method)) AS payment_method,
    amount,
    LOWER(TRIM(status)) AS status,
    payment_date,
    updated_at
FROM {{ source('shopflow', 'payments') }}