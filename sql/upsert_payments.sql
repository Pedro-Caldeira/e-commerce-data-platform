Insert into payments (
    payment_id,
    order_id,
    payment_method,
    amount,
    status,
    payment_date,
    updated_at
)
Select
    payment_id,
    order_id,
    payment_method,
    amount,
    status,
    payment_date,
    updated_at
From payments_staging
On Conflict (payment_id)
Do Update Set
    order_id = EXCLUDED.order_id,
    payment_method = EXCLUDED.payment_method,
    amount = EXCLUDED.amount,
    status = EXCLUDED.status,
    payment_date = EXCLUDED.payment_date,
    updated_at = EXCLUDED.updated_at;