class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_URL = '/api/v1/courier'
    LOGIN_URL = '/api/v1/courier/login'
    ORDER_URL = '/api/v1/orders'
    ACCEPT_ORDER = '/api/v1/orders/accept'
    GET_ORDER = '/api/v1/orders/track'


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

