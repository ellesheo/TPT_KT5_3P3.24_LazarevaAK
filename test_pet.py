from http import HTTPStatus

import allure

from api import PetClient
from assertions import assert_pet, assert_status_code, validate_schema
from models import ApiResponse, Pet


@allure.feature("Pet")
@allure.story("Pet API")
class TestPet:
    @allure.title("Добавление питомца")
    def test_create_pet(self, class_pet_client: PetClient):
        payload = Pet()

        response = class_pet_client.create_pet_api(payload)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_pet(response.json(), payload)
        validate_schema(response.json(), Pet.model_json_schema())

    @allure.title("Получение питомца по id")
    def test_get_pet(self, class_pet_client: PetClient, function_pet: Pet):
        response = class_pet_client.get_pet_api(function_pet.id)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_pet(response.json(), function_pet)
        validate_schema(response.json(), Pet.model_json_schema())

    @allure.title("Изменение питомца")
    def test_update_pet(self, class_pet_client: PetClient, function_pet: Pet):
        function_pet.name = "Кутузик"
        function_pet.status = "sold"

        response = class_pet_client.update_pet_api(function_pet)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_pet(response.json(), function_pet)
        validate_schema(response.json(), Pet.model_json_schema())

    @allure.title("Удаление питомца")
    def test_delete_pet(self, class_pet_client: PetClient, function_pet: Pet):
        delete_response = class_pet_client.delete_pet_api(function_pet.id)
        get_response = class_pet_client.get_pet_api(function_pet.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)
        validate_schema(delete_response.json(), ApiResponse.model_json_schema())
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
