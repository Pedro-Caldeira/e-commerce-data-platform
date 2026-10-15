SELECT
    customer_id,
    TRIM(name) AS name,
    LOWER(TRIM(email)) AS email,
    country,
    created_at,
    updated_at
FROM {{ source('shopflow', 'customers') }}