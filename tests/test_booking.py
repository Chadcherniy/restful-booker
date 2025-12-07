import requests
import allure

@allure.feature("Booking")
@allure.story("Get booking ids")
def test_get_booking_ids(base_url):
    with allure.step('Получаем все айди'):
        r = requests.get(url=f'{base_url}/booking')

    with allure.step("Verify status code is 200"):
        assert r.status_code == 200

    with allure.step("Verify response is a non-empty list"):
        data = r.json()
        assert isinstance(data, list), "Response is not a list"

    with allure.step("Verify each item has 'bookingid' as integer"):
        for item in data:
            assert "bookingid" in item, "Missing 'bookingid' in booking"
            assert isinstance(item["bookingid"], int), "'bookingid' is not an integer"
