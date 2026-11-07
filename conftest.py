import pytest

from api import PetClient, StoreClient
from client import HTTPClient
from models import Order, Pet
from settings import base_settings


@pytest.fixture(scope="class")
def class_pet_client() -> PetClient:
    return PetClient(client=HTTPClient(base_url=base_settings.base_url))


@pytest.fixture(scope="class")
def class_store_client() -> StoreClient:
    return StoreClient(client=HTTPClient(base_url=base_settings.base_url))


@pytest.fixture
def function_pet(class_pet_client: PetClient) -> Pet:
    pet = class_pet_client.create_pet()
    yield pet
    class_pet_client.delete_pet_api(pet.id)


@pytest.fixture
def function_order(class_store_client: StoreClient) -> Order:
    order = class_store_client.create_order()
    yield order
    class_store_client.delete_order_api(order.id)
