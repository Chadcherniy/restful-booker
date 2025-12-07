# tests/test_auth.py
import requests
import allure

@allure.feature("Authentication")
@allure.story("User can obtain an auth token")
def test_create_auth_token(base_url):    #Вставляем из conftest.py фикстуру
    # Given
    payload = {"username": "admin", "password": "password123"}
    headers = {"Content-Type": "application/json"}

    # When
    with allure.step("Send POST request to /auth"):
        response = requests.post(
            url=f"{base_url}/auth",
            json=payload,
            headers=headers
        )

    # Then
    with allure.step("Verify status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify response contains 'token'"):
        data = response.json()
        assert "token" in data
        assert isinstance(data["token"], str)
        assert len(data["token"]) > 0
