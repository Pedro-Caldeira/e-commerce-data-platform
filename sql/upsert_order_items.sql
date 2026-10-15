INSERT INTO order_items (
    order_id,
    product_id,
    quantity,
    unit_price,
    line_total
)
SELECT
    order_id,
    product_id,
    quantity,
    unit_price,
    line_total
FROM order_items_staging
ON CONFLICT (order_id, product_id)
DO UPDATE SET
    quantity = EXCLUDED.quantity,
    unit_price = EXCLUDED.unit_price,
    line_total = EXCLUDED.line_total;