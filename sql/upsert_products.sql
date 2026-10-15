insert into products (
    product_id,
    name,
    category,
    price,
    stock,
    created_at,
    updated_at
)
select
    product_id,
    name,
    category,
    price,
    stock,
    created_at,
    updated_at
from products_staging
on conflict (product_id)
do update set
    name = EXCLUDED.name,
    category = EXCLUDED.category,
    price = EXCLUDED.price,
    stock = EXCLUDED.stock,
    created_at = EXCLUDED.created_at,
    updated_at = EXCLUDED.updated_at;