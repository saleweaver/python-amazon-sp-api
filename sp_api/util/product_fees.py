def create_fees_body(
    *,
    price,
    shipping_price=None,
    currency="USD",
    is_fba=False,
    identifier=None,
    points=None,
    marketplace_id=None,
    optional_fulfillment_program=None,
    id_type=None,
    id_value=None,
):
    body = {
        "FeesEstimateRequest": {
            "Identifier": identifier or str(price),
            "PriceToEstimateFees": {
                "ListingPrice": {"Amount": price, "CurrencyCode": currency},
                "Shipping": (
                    {"Amount": shipping_price, "CurrencyCode": currency}
                    if shipping_price
                    else None
                ),
                "Points": points or None,
            },
            "IsAmazonFulfilled": is_fba,
            "OptionalFulfillmentProgram": (
                optional_fulfillment_program
                if is_fba is True and optional_fulfillment_program
                else None
            ),
            "MarketplaceId": marketplace_id,
        }
    }

    if id_type and id_value:
        body["IdType"] = id_type
        body["IdValue"] = id_value

    return body
