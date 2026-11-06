import allure
import pytest

from base_request import BASE_URL, BaseRequest
from models import ApiResponse, Pet

api = BaseRequest(BASE_URL)


@pytest.fixture
def pet():
    return Pet(id=332419, name="Муртузик")


@allure.feature("Pet")
@allure.title("Добавление питомца")
def test_post_pet(pet):
    response = api.post("pet", pet.model_dump())
    assert response.status_code == 200
    assert Pet.model_validate(response.json()) == pet


@allure.feature("Pet")
@allure.title("Получение питомца по id")
def test_get_pet(pet):
    response = api.get(f"pet/{pet.id}")
    assert response.status_code == 200
    result = Pet.model_validate(response.json())
    assert result.name == "Муртузик"
    assert result.category.name == "cats"


@allure.feature("Pet")
@allure.title("Изменение питомца")
def test_put_pet(pet):
    pet.name = "Кутузик"
    pet.status = "sold"
    response = api.put("pet", pet.model_dump())
    assert response.status_code == 200
    result = Pet.model_validate(response.json())
    assert result.name == "Кутузик"
    assert result.status == "sold"


@allure.feature("Pet")
@allure.title("Удаление питомца")
def test_delete_pet(pet):
    response = api.delete(f"pet/{pet.id}")
    assert response.status_code == 200
    assert ApiResponse.model_validate(response.json()).message == str(pet.id)
    response = api.get(f"pet/{pet.id}", expected_status=404)
    assert response.status_code == 404
