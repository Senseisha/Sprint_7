import allure
import pytest
import helper
import tests.conftest

@allure.title('Test Successful Orders Creation')
@pytest.mark.parametrize('color', [BLACK, GREY, BLACK GREY, None])
def test_create_orders_with_different_colors(self, order_methods, color,):
    body = helper.modify_create_order_body()
