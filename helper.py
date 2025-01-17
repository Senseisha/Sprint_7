from data import DataForCreateOrder


def modify_create_order_body(key, value):
    body = DataForCreateOrder.CREATE_ORDER.copy()

    if value == None:
        del body[key]
    else:
        body[key] = value

    return body
