SELECT
    order_id,
    product_id,
    quantity,
    unit_price,
    line_total
FROM {{ source('shopflow', 'order_items') }}