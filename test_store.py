import allure
import pytest

from base_request import BASE_URL, BaseRequest
from models import ApiResponse, Order

api = BaseRequest(BASE_URL)


@pytest.fixture
def order():
    return Order(id=3324, petId=332419, quantity=2)


@allure.feature("Store")
@allure.title("Создание заказа")
def test_post_order(order):
    response = api.post("store/order", order.model_dump(exclude_none=True))
    assert response.status_code == 200
    result = Order.model_validate(response.json())
    assert result.id == order.id
    assert result.status == "placed"


@allure.feature("Store")
@allure.title("Получение заказа по id")
def test_get_order(order):
    response = api.get(f"store/order/{order.id}")
    assert response.status_code == 200
    result = Order.model_validate(response.json())
    assert result.petId == order.petId
    assert result.quantity == 2


@allure.feature("Store")
@allure.title("Получение остатков магазина")
def test_get_inventory():
    response = api.get("store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@allure.feature("Store")
@allure.title("Удаление заказа")
def test_delete_order(order):
    response = api.delete(f"store/order/{order.id}")
    assert response.status_code == 200
    assert ApiResponse.model_validate(response.json()).message == str(order.id)
    response = api.get(f"store/order/{order.id}", expected_status=404)
    assert response.status_code == 404
