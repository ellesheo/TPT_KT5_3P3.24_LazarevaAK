import json
import time

import allure
import requests

BASE_URL = "https://petstore.swagger.io/v2"


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, method, endpoint, data=None, expected_status=200):
        url = f"{self.base_url}/{endpoint}"
        with allure.step(f"{method} {url}"):
            for _ in range(5):
                response = requests.request(method, url, json=data)
                if response.status_code == expected_status:
                    break
                time.sleep(1)
            if data:
                allure.attach(json.dumps(data, ensure_ascii=False), "request", allure.attachment_type.JSON)
            allure.attach(response.text, "response", allure.attachment_type.JSON)
        return response

    def get(self, endpoint, expected_status=200):
        return self._request("GET", endpoint, expected_status=expected_status)

    def post(self, endpoint, data):
        return self._request("POST", endpoint, data)

    def put(self, endpoint, data):
        return self._request("PUT", endpoint, data)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)
