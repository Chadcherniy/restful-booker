import pytest
import requests
import allure

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
headers = {"Content-Type": "application/json"}
@allure.feature("Booking")
@allure.story("Booking CRUD")
@allure.title("Создаем бронь, Получаем ID, Обновляем и Удаляем")
def test_crud_booking(base_url, auth_token):    # Интеграционный тест
    # 1. CREATE\Создаем
    with allure.step('Создаем бронь'):
        create_resp = requests.post(
            f'{base_url}/booking',
            json=VALID_BOOKING,
        )   # Делаем post-запрос с валидными данными
        assert create_resp.status_code == 200, 'Прошло не так'
        booking_id = create_resp.json()["bookingid"]    # записываем айди в переменную bokking_id

    # 2. READ\Читаем
    with allure.step("Получаем бронь по ID"):
        get_resp = requests.get(f"{base_url}/booking/{booking_id}")
        assert get_resp.status_code == 200    # Проверяем статус-код
        assert get_resp.json()["firstname"] == "Герман" # Проверяем, что зарегистрировали клиента с именем Герман

    # 3. UPDATE (PUT)
    updated_data = VALID_BOOKING.copy()
    updated_data["totalprice"] = 200
    updated_data["additionalneeds"] = "Lunch"

    with allure.step("Обновляем данные в брони через PUT"):
        put_resp = requests.put(
            f"{base_url}/booking/{booking_id}",
            json=updated_data,
            headers={"Cookie": f"token={auth_token}"}
        )
        assert put_resp.status_code == 200
        assert put_resp.json()["totalprice"] == 200

    # 4. DELETE
    with allure.step("Delete the booking"):
        del_resp = requests.delete(
            f"{base_url}/booking/{booking_id}",
            headers={"Cookie": f"token={auth_token}"}
        )
        assert del_resp.status_code == 201  # Да, бронь удалена