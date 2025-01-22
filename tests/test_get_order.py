import allure
import pytest
import helper
from data import DataForResponse


class TestGetOrder:
    @allure.title('Test Success Get Order')
    @pytest.mark.parametrize('colors', [['GREY']])
    def test_success_get_order(self, order_methods, colors, create_courier, courier_methods):
        body = helper.modify_create_order_body('color', colors)
        order_id = order_methods.create_order(body).json().get('track')
        response = order_methods.get_order_number(order_id)
        assert response.status_code == 200 and response.json()['order']

    @allure.title('Test Unsuccess Get Order without track')
    def test_get_order_without_track(self, order_methods):
        order_id = ''
        response = order_methods.get_order_number(order_id)
        assert response.status_code == 400 and response.json()['message'] == DataForResponse.not_enough_data

    @allure.title('Test Unsuccess Get Order with wrong track')
    def test_get_order_with_wrong_track(self, order_methods):
        order_id = '001100'
        response = order_methods.get_order_number(order_id)
        assert response.status_code == 404 and response.json()['message'] == DataForResponse.order_not_found
