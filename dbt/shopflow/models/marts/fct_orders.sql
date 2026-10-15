WITH order_items_agg AS (
    SELECT
        order_id,
        COUNT(*) AS number_of_order_lines,
        SUM(quantity) AS total_units,
        SUM(line_total) AS items_total
    FROM {{ ref('stg_order_items') }}
    GROUP BY order_id
),

payments_agg AS (
    SELECT
        order_id,
        SUM(amount) AS payments_total,
        COUNT(*) AS number_of_payments
    FROM {{ ref('stg_payments') }}
    GROUP BY order_id
)

SELECT
    o.order_id,
    o.customer_id,
    c.name AS customer_name,
    c.country AS customer_country,
    o.order_date,
    o.status AS order_status,
    o.total_amount AS order_total,

    COALESCE(i.number_of_order_lines, 0) AS number_of_order_lines,
    COALESCE(i.total_units, 0) AS total_units,
    COALESCE(i.items_total, 0) AS items_total,

    COALESCE(p.payments_total, 0) AS payments_total,
    COALESCE(p.number_of_payments, 0) AS number_of_payments,

    o.total_amount - COALESCE(p.payments_total, 0)
        AS payment_difference

FROM {{ ref('stg_orders') }} AS o
LEFT JOIN {{ ref('stg_customers') }} AS c
    ON o.customer_id = c.customer_id
LEFT JOIN order_items_agg AS i
    ON o.order_id = i.order_id
LEFT JOIN payments_agg AS p
    ON o.order_id = p.order_id