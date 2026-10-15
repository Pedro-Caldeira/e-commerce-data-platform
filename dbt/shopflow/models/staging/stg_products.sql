select product_id,
       TRIM(name) as name,
       TRIM(category) as category,
       price,
       stock,
       created_at,
       updated_at
from {{ source('shopflow','products') }}