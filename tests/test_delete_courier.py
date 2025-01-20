import allure


class TestDeleteCourier:
    @allure.title('Test Successful Deletion of creation')
    def test_successful_deletion_of_creation(self, courier_methods, create_courier):
        courier_id = courier_methods.login_courier(create_courier["login"], \
                                                   create_courier["password"]).json().get("id")
        delete_creation_response = courier_methods.delete_courier(courier_id)
        assert delete_creation_response.status_code == 200 and delete_creation_response.json()['ok'] is True

    @allure.title('Test Unsuccessful Deletion of creation without id')
    def test_deletion_without_id(self, courier_methods, create_courier):
        courier_id = ''
        courier_methods.login_courier(create_courier["login"], \
                                                create_courier["password"]).json().get("id")
        response = courier_methods.delete_courier(courier_id)
        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для удаления курьера"

    @allure.title('Test Unsuccessful Deletion of creation with non-existent id')
    def test_deletion_with_nonexistent_id(self, courier_methods, create_courier):
        courier_id = '0001'
        courier_methods.login_courier(create_courier["login"], \
                                      create_courier["password"]).json().get("id")
        response = courier_methods.delete_courier(courier_id)
        assert response.status_code == 404 and response.json()['message'] == "Курьера с таким id нет."