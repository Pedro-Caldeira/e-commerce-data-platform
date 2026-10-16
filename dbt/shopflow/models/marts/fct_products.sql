
WITH product_sales AS (
    SELECT
        product_id,
        COUNT(DISTINCT order_id) AS number_of_orders,
        SUM(quantity) AS units_sold,
        SUM(line_total) AS revenue
    FROM {{ ref('int_order_items_enriched') }}
    GROUP BY product_id
)

SELECT
    p.product_id,
    p.name AS product_name,
    p.category,
    p.price AS current_price,
    p.stock AS current_stock,

    COALESCE(s.number_of_orders, 0) AS number_of_orders,
    COALESCE(s.units_sold, 0) AS units_sold,
    COALESCE(s.revenue, 0) AS revenue

FROM {{ ref('stg_products') }} AS p

LEFT JOIN product_sales AS s
    ON p.product_id = s.product_id
