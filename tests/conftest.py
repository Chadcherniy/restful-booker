# tests/conftest.py
import pytest
import requests
from src.api.auth_client import AuthClient
from src.api.booking_client import BookingClient
from config.settings import BASE_URL

# Возвращаем главный урл
@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

# Возвращаем полученный токен
@pytest.fixture(scope="session")
def auth_token():
    client = AuthClient()
    return client.create_token()

# Получаем данные о броне
@pytest.fixture(scope="session")
def booking_client(auth_token):
    return BookingClient(token=auth_token)

# Given
VALID_BOOKING = {
    "firstname": "Герман",
    "lastname": "Патриков",
    "totalprice": 100,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-12-01",
        "checkout": "2025-12-10"
    },
    "additionalneeds": "Breakfast"
}