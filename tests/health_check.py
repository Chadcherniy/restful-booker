import requests
import allure


@allure.feature("Ping")
@allure.story("HealthCheck")
@allure.title("Проверка работоспособности ресурса")
def test_health_check(base_url):
    with allure.step('Проверяем отклик ресурса'):
        resp = requests.get(f'{base_url}/ping')
        assert resp.status_code == 201
