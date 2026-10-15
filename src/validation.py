
def validate_data(
    data: list[dict],
    dataset: str
) -> list[dict]:

    required_fields = {
        "customers": [
            "customer_id",
            "name",
            "email"
        ],
        "products": [
            "product_id",
            "name",
            "price"
        ],
        "orders": [
            "order_id",
            "customer_id",
            "total_amount"
        ],
        "payments": [
            "payment_id",
            "order_id",
            "amount",
            "status"
        ]
    }
    
    valid_data = []
    invalid_data = []

    fields = required_fields[dataset]

    for item in data:

        item_errors = []

        for field in fields:

            if field not in item or item[field] is None:
                item_errors.append(field)

        if item_errors:
            invalid_data.append({
                "record": item,
                "errors": item_errors
            })
        else:
            valid_data.append(item)

    return valid_data, invalid_data

    