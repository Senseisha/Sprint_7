class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_URL = '/api/v1/courier'
    LOGIN_URL = '/api/v1/courier/login'
    ORDER_URL = '/api/v1/orders'
    ACCEPT_ORDER = '/api/v1/orders/accept'
    GET_ORDER = '/api/v1/orders/track'


class DataForResponse:
    login_in_use = "Этот логин уже используется. Попробуйте другой."
    not_enough_data_to_create = "Недостаточно данных для создания учетной записи"
    account_not_found = "Учетная запись не найдена"
    not_enough_data = "Недостаточно данных для поиска"
    order_not_found = "Заказ не найден"
    not_enough_data_to_delete = "Недостаточно данных для удаления курьера"
    no_courier_with_this_id = "Курьера с таким id нет."
    not_courier_with_this_id = "Курьера с таким id не существует"
    no_order_with_this_id = "Заказа с таким id не существует"


class DataForCreate:
    CREATE_COURIER_BODY = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }


class DataForLogin:
    COURIER_LOGIN = {
        "login": "ninja",
        "password": "1234"
    }


class DataForCreateOrder:
    CREATE_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
