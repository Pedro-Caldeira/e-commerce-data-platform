SELECT
    oi.order_id,
    oi.product_id,
    p.name AS product_name,
    p.category,
    oi.quantity,
    oi.unit_price,
    oi.line_total
FROM {{ ref('stg_order_items') }} AS oi
LEFT JOIN {{ ref('stg_products') }} AS p
    ON oi.product_id = p.product_id