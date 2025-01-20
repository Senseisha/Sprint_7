import allure
import pytest
import helper


class TestAcceptOrder:
    @allure.title('Test Successful Order Accept')
    @pytest.mark.parametrize('colors', [['GREY']])
    def test_successful_order_accept(self, order_methods, colors, courier_methods, create_login_delete_courier):
        body = helper.modify_create_order_body('color', colors)
        order_id = order_methods.create_order(body).json().get('track')

        response = order_methods.accept_order(order_id, create_login_delete_courier)
        assert response.status_code == 200 and response.json()['ok'] is True

    @allure.title('Test Unsuccessful Order Accept without courier id')
    @pytest.mark.parametrize('colors', [['BLACK']])
    def test_order_accept_without_courier_id(self, order_methods, courier_methods, create_courier, colors):
        body = helper.modify_create_order_body('color', colors)
        order_id = order_methods.create_order(body).json().get('track')
        response = order_methods.accept_order(order_id)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Test Unsuccessful Order Accept with wrong courier id')
    @pytest.mark.parametrize('colors', [['BLACK']])
    def test_order_accept_with_wrong_courier_id(self, order_methods, courier_methods, create_courier, colors):
        body = helper.modify_create_order_body('color', colors)
        order_id = order_methods.create_order(body).json().get('track')
        wrong_courier_id = '001010'
        response = order_methods.accept_order(order_id, wrong_courier_id)
        assert response.status_code == 404 and response.json()['message'] == 'Курьера с таким id не существует'

    @allure.title('Test Unsuccessful Order Accept without order id')
    def test_order_accept_without_order_id(self, order_methods, courier_methods, create_login_delete_courier):
        order_id = ''
        response = order_methods.accept_order(order_id, create_login_delete_courier)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Test Unsuccessful Order Accept with wrong order id')
    def test_order_accept_with_wrong_order_id(self, order_methods, courier_methods, create_login_delete_courier):
        order_id = '000'
        response = order_methods.accept_order(order_id, create_login_delete_courier)
        assert response.status_code == 404 and response.json()['message'] == 'Заказа с таким id не существует'
