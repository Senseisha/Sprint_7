import allure


class TestLoginCourier:
    @allure.title('Test Successful Courier Login')
    def test_successful_courier_login(self, generate_couriers_data, courier_methods):
        courier_login = courier_methods\
            .login_courier(generate_couriers_data["login"], generate_couriers_data["password"])
        login_id = courier_login.json()["id"]
        assert courier_login.status_code == 200 and login_id
        with allure.step('Clear Up - delete login courier after test'):
            courier_methods.delete_courier(login_id)

    @allure.title('Test Unsuccessful Courier Login with wrong password')
    def test_courier_login_with_wrong_login(self, generate_couriers_data, courier_methods):
        wrong_password = " "
        courier_login = courier_methods\
            .login_courier(generate_couriers_data["login"], wrong_password)
        assert courier_login.status_code == 404 and courier_login.json()['message'] == "Учетная запись не найдена"

    @allure.title('Test Unsuccessful Courier Login with non-existent user')
    def test_courier_login_with_nonexistent_user(self, generate_couriers_data, courier_methods):
        nonexistent_login = " "
        courier_login = courier_methods \
            .login_courier(nonexistent_login, generate_couriers_data["password"])
        assert courier_login.status_code  == 404 and courier_login.json()['message'] == "Учетная запись не найдена"
