import allure
import pytest
import helper


class TestCreateOrders:
    @allure.title('Test Successful Orders Creation')
    @pytest.mark.parametrize('colors', ['BLACK', 'GREY', 'BLACK, GREY', None])
    def test_create_orders_with_different_colors(self, order_methods, color):
        body = helper.modify_create_order_body('color', colors)
        response = order_methods.create_order(body)
        assert response.
