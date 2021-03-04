
from sp_api.base.helpers import nest_dict


def get_shipment_request_details(order_data: dict):

    data = dict()
    data["AmazonOrderId"] = ""
    data["ItemList"] = []
    data["ShipFromAddress.Name"] = order_data['shop_name']
    data["ShipFromAddress.AddressLine1"] = order_data['shop_address1']
    data["ShipFromAddress.Email"] = order_data['shop_email']
    data["ShipFromAddress.City"] = order_data['shop_city']
    data["ShipFromAddress.PostalCode"] = order_data['shop_postal']
    data["ShipFromAddress.CountryCode"] = order_data['shop_country']
    data["ShipFromAddress.Phone"] = order_data['shop_phone']
    data["PackageDimensions.Length"] = str(round(order_data['order_pkg_length'], 1))
    data["PackageDimensions.Width"] = str(round(order_data['order_pkg_width'], 1))
    data["PackageDimensions.Height"] = str(round(order_data['order_pkg_height'], 1))
    data["PackageDimensions.Unit"] = 'inches'
    data["Weight.Value"] = str(round(order_data['order_pkg_weight'], 1))
    data["Weight.Unit"] = "ounces"
    data["ShippingServiceOptions.DeliveryExperience"] = order_data['delivery_experience']
    data["ShippingServiceOptions.CarrierWillPickup"] = order_data['carrier_will_pickup']

    lines = order_data.get("lines", [])
    for line in lines:
        data["ItemList"].append(
            {
                "OrderItemId": line['client_line_id'],
                "Quantity": line['quantity']
            }
        )

    addr2 = order_data.get("shop_address2", None)
    if addr2:
        data["ShipFromAddress.AddressLine2"] = addr2

    addr3 = order_data.get("shop_address3", None)
    if addr3:
        data["ShipFromAddress.AddressLine3"] = addr3

    ship_date = order_data.get("ship_date", None)
    if ship_date:
        data["ShipDate"] = ship_date

    seller_order_id = order_data.get("seller_order_id", None)
    if seller_order_id:
        data["SellerOrderId"] = seller_order_id

    must_arrive_date = order_data.get("must_arrive_date", None)
    if must_arrive_date:
        data["MustArriveByDate"] = must_arrive_date

    custom_text_for_label = order_data.get("custom_text_for_label", None)
    standard_id_for_label = order_data.get("standard_id_for_label", None)

    if custom_text_for_label or standard_id_for_label:
        data["LabelCustomization"] = {}
        if custom_text_for_label:
            data["LabelCustomization.CustomTextForLabel"] = custom_text_for_label

        if standard_id_for_label:
            data["LabelCustomization.StandardIdForLabel"] = standard_id_for_label

    return nest_dict(data)
