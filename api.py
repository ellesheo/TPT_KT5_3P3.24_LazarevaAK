from enum import Enum

import allure
from httpx import Response

from client import APIClient
from models import Order, Pet


class APIRoutes(str, Enum):
    PET = "/pet"
    ORDER = "/store/order"
    INVENTORY = "/store/inventory"

    def __str__(self):
        return self.value


class PetClient(APIClient):
    @allure.step("Добавление питомца")
    def create_pet_api(self, payload: Pet) -> Response:
        return self.client.post(APIRoutes.PET, json=payload.model_dump(by_alias=True))

    @allure.step("Получение питомца с id {pet_id}")
    def get_pet_api(self, pet_id: int) -> Response:
        return self.client.get(f"{APIRoutes.PET}/{pet_id}")

    @allure.step("Изменение питомца")
    def update_pet_api(self, payload: Pet) -> Response:
        return self.client.put(APIRoutes.PET, json=payload.model_dump(by_alias=True))

    @allure.step("Удаление питомца с id {pet_id}")
    def delete_pet_api(self, pet_id: int) -> Response:
        return self.client.delete(f"{APIRoutes.PET}/{pet_id}")

    def create_pet(self) -> Pet:
        response = self.create_pet_api(Pet())
        return Pet(**response.json())


class StoreClient(APIClient):
    @allure.step("Создание заказа")
    def create_order_api(self, payload: Order) -> Response:
        return self.client.post(APIRoutes.ORDER, json=payload.model_dump(by_alias=True))

    @allure.step("Получение заказа с id {order_id}")
    def get_order_api(self, order_id: int) -> Response:
        return self.client.get(f"{APIRoutes.ORDER}/{order_id}")

    @allure.step("Получение остатков магазина")
    def get_inventory_api(self) -> Response:
        return self.client.get(APIRoutes.INVENTORY)

    @allure.step("Удаление заказа с id {order_id}")
    def delete_order_api(self, order_id: int) -> Response:
        return self.client.delete(f"{APIRoutes.ORDER}/{order_id}")

    def create_order(self) -> Order:
        response = self.create_order_api(Order())
        return Order(**response.json())
