import allure
from data import DataForResponse


class TestCreateCourier:
    @allure.title('Test successful Courier Creation')
    def test_success_created_courier(self, generate_couriers_data_with_delete, courier_methods):
        courier_response = courier_methods.create_courier(generate_couriers_data_with_delete)
        assert courier_response.status_code == 201 and courier_response.json()['ok'] is True

    @allure.title('Test Unsuccessful Creating two identical couriers')
    def test_creating_two_identical_couriers(self, generate_couriers_data_with_delete, courier_methods):
        courier_methods.create_courier(generate_couriers_data_with_delete)
        same_courier_response = courier_methods.create_courier(generate_couriers_data_with_delete)
        assert same_courier_response.status_code == 409 \
               and same_courier_response.json()['message'] == DataForResponse.login_in_use

    @allure.title('Test Unsuccessful Creating Courier without one field')
    def test_creating_courier_without_one_field(self, generate_couriers_data_with_delete, courier_methods):
        copy_data = generate_couriers_data_with_delete.copy()
        copy_data['login'] = ''
        courier_response = courier_methods.create_courier(copy_data)
        assert courier_response.status_code == 400 \
               and courier_response.json()['message'] == DataForResponse.not_enough_data_to_create

