import pytest

from generator import register_new_courier
from methods.courier_methods import CourierMethods
from methods.orders_methods import OrderMethods


@pytest.fixture()
def order_methods():
    return OrderMethods()


@pytest.fixture()
def courier_methods():
    return CourierMethods()


@pytest.fixture()
def generate_couriers_data_with_delete():
    create_couriers_body = register_new_courier()
    login = create_couriers_body['login']
    password = create_couriers_body['password']
    yield create_couriers_body
    courier_id = CourierMethods().login_courier(login, password).json().get('id')
    if courier_id:
        CourierMethods().delete_courier(courier_id)


@pytest.fixture()
def generate_couriers_data():
    create_couriers_body = register_new_courier()
    CourierMethods().create_courier(create_couriers_body)
    yield create_couriers_body
