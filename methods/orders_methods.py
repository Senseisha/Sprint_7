import requests
from data import Url


class OrderMethods:
    def create_order(self, body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=body)

    def get_list_of_orders(self):
        return requests.get(f'{Url.BASE_URL}{Url.ORDER_URL}')

    def accept_order(self, order_id, courier_id=None):
        if courier_id:
            params = {'courierId': courier_id}
        else:
            params = {}
        return requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER}/{order_id}', params=params)

    def get_order_number(self, track, track_number):
        params = {'t': track_number}
        return requests.get(f'{Url.BASE_URL}{Url.GET_ORDER}/{track}', params=params)