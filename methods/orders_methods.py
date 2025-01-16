import requests

from data import Url, DataForCreateOrder


class OrderMethods:
    def create_order(self):
        response = requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=DataForCreateOrder.CREATE_ORDER)
        return response.json()[track]