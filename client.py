import time
from http import HTTPStatus

import allure
from httpx import Client


class HTTPClient(Client):
    def request(self, method, url, **kwargs):
        for _ in range(5):
            response = super().request(method, url, **kwargs)
            if response.status_code == HTTPStatus.OK:
                break
            time.sleep(1)
        return response

    @allure.step("GET {url}")
    def get(self, url, **kwargs):
        return super().get(url, **kwargs)

    @allure.step("POST {url}")
    def post(self, url, **kwargs):
        return super().post(url, **kwargs)

    @allure.step("PUT {url}")
    def put(self, url, **kwargs):
        return super().put(url, **kwargs)

    @allure.step("DELETE {url}")
    def delete(self, url, **kwargs):
        return super().delete(url, **kwargs)


class APIClient:
    def __init__(self, client: HTTPClient):
        self._client = client

    @property
    def client(self) -> HTTPClient:
        return self._client
