import allure
import pytest
import helper


class TestCreateOrders:
    @allure.title('Test Successful Orders Creation')
    @pytest.mark.parametrize('colors', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], None])
    def test_create_orders_with_different_colors(self, order_methods, colors):
        body = helper.modify_create_order_body('color', colors)
        print(body)
        response = order_methods.create_order(body)
        assert response.status_code == 201 and response.json()['track']


class TestGetListOfOrders:
    @allure.title('Test Successful Get a list of orders')
    def test_get_list_of_orders(self, order_methods):
        response = order_methods.get_list_of_orders()
        assert response.status_code == 200 and response.json()['orders']

