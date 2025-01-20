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
def generate_courier_data():
    create_couriers_body = register_new_courier()
    return create_couriers_body


@pytest.fixture()
def generate_couriers_data_with_delete(generate_courier_data):
    yield generate_courier_data

    login = generate_courier_data['login']
    password = generate_courier_data['password']
    courier_id = CourierMethods().login_courier(login, password).json().get('id')
    if courier_id:
        CourierMethods().delete_courier(courier_id)


@pytest.fixture()
def create_courier(generate_courier_data):
    CourierMethods().create_courier(generate_courier_data)
    yield generate_courier_data


@pytest.fixture()
def create_login_delete_courier(generate_courier_data):
    login = generate_courier_data['login']
    password = generate_courier_data['password']
    CourierMethods().create_courier(generate_courier_data)

    courier_id = CourierMethods().login_courier(login, password).json().get('id')

    yield courier_id

    CourierMethods().delete_courier(courier_id)
