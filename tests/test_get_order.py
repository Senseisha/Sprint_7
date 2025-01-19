import allure
from data import DataForCreateOrder


class TestGetOrder:
    @allure.title('Test Success Get Order')
    def test_success_get_order(self, order_methods):
        create = DataForCreateOrder()
        order_track = order_methods.create_order(create)
        response = order_methods.get_order_number(order_track)
        assert response.status_code == 200 and response.json()['order']

