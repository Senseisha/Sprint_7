from data import DataForCreateOrder


def modify_create_order_body(key, value):
    body = DataForCreateOrder.CREATE_ORDER.copy()
    body[key] = value
    return body
