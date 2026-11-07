import allure
from jsonschema import validate

from models import Order, Pet


@allure.step("Проверка статус кода")
def assert_status_code(actual: int, expected: int):
    assert actual == expected


@allure.step("Проверка JSON схемы")
def validate_schema(instance: dict, schema: dict):
    validate(instance=instance, schema=schema)


@allure.step("Проверка питомца")
def assert_pet(expected_pet: dict, actual_pet: Pet):
    assert expected_pet["id"] == actual_pet.id
    assert expected_pet["name"] == actual_pet.name
    assert expected_pet["category"]["name"] == actual_pet.category.name
    assert expected_pet["status"] == actual_pet.status


@allure.step("Проверка заказа")
def assert_order(expected_order: dict, actual_order: Order):
    assert expected_order["id"] == actual_order.id
    assert expected_order["petId"] == actual_order.pet_id
    assert expected_order["quantity"] == actual_order.quantity
    assert expected_order["status"] == actual_order.status
