import requests
from data import Url, DataForLogin


class CourierMethods:
    def create_courier(self, body):
        print(body)
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_URL}', data=body)

    def login_courier(self, login, password):
        payload = {'login': login, 'password': password}
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data=payload)

    def delete_courier(self, courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.CREATE_URL}/{courier_id}')
