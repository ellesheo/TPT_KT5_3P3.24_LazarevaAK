from http import HTTPStatus

import allure

from api import StoreClient
from assertions import assert_order, assert_status_code, validate_schema
from models import ApiResponse, Inventory, Order


@allure.feature("Store")
@allure.story("Store API")
class TestStore:
    @allure.title("Создание заказа")
    def test_create_order(self, class_store_client: StoreClient):
        payload = Order()

        response = class_store_client.create_order_api(payload)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_order(response.json(), payload)
        validate_schema(response.json(), Order.model_json_schema())

    @allure.title("Получение заказа по id")
    def test_get_order(self, class_store_client: StoreClient, function_order: Order):
        response = class_store_client.get_order_api(function_order.id)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_order(response.json(), function_order)
        validate_schema(response.json(), Order.model_json_schema())

    @allure.title("Получение остатков магазина")
    def test_get_inventory(self, class_store_client: StoreClient):
        response = class_store_client.get_inventory_api()

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_schema(response.json(), Inventory.model_json_schema())

    @allure.title("Удаление заказа")
    def test_delete_order(self, class_store_client: StoreClient, function_order: Order):
        delete_response = class_store_client.delete_order_api(function_order.id)
        get_response = class_store_client.get_order_api(function_order.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)
        validate_schema(delete_response.json(), ApiResponse.model_json_schema())
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
