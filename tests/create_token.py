import allure
import pytest
import requests

def create_token():
    with allure.step('Получаем токен для авторизации'):
        r = requests.post('https://restful-booker.herokuapp.com/auth', body)
        
        body = {
            "username" : "admin",
            "password" : "password123"
            }

@allure.feature("Users")
@allure.story("Get user by ID")
def test_get_user_by_id(api_client):
    with allure.step("Send GET request to /users/1"):
        response = api_client.get("users/1")

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify response contains 'id'"):
        assert "id" in response.json()