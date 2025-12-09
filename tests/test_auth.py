# tests/test_auth.py
import requests
import allure
from src.api.auth_client import AuthClient

@allure.feature("Authentication")
@allure.story("User can obtain an auth token")
@allure.title("Проверка получения токена с корректными данными") 
def test_create_auth_token():
    client = AuthClient()
    token = client.create_token()
    assert isinstance(token, str)
    assert len(token) > 0
