# tests/conftest.py
import pytest
import requests
from config.settings import BASE_URL

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def auth_token(base_url):
    resp = requests.post(
        f"{base_url}/auth",
        json={"username": "admin", "password": "password123"}
    )
    assert resp.status_code == 200
    return resp.json()["token"]