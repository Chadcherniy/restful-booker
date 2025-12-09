import requests
from config.settings import BASE_URL

class BookingClient:
    def __init__(self, token=None):
        self.base_url = BASE_URL
        self.token = token
        
    def _get_headers(self): # Получаем заголовки
        headers = {"Content-Type": "application/json"}
        if self.token:  #Если токен был получен, то подставляем токен в Куки
            headers["Cookie"] = f"token={self.token}"
        return headers
    
    def create_booking(self, booking_data):     #Создаем бронь
        response = requests.post(
            f"{self.base_url}/booking",
            json=booking_data,
            headers=self._get_headers()
        )
        response.raise_for_status()
        return response.json()
    
    def get_booking(self, booking_id):  #Получаем id брони
        response = requests.get(f"{self.base_url}/booking/{booking_id}")
        response.raise_for_status()
        return response.json()
    
    def get_all_bookings(self, params=None):    #Получаем все брони 
        response = requests.get(f"{self.base_url}/booking", params=params)
        response.raise_for_status()
        return response.json()
    
    def update_booking(self, booking_id, booking_data): #Обновляем данные в брони 
        response = requests.put(
            f"{self.base_url}/booking/{booking_id}",
            json=booking_data,
            headers=self._get_headers()                    
            )
        response.raise_for_status()
        return response.json()
    
    def delete_booking(self, booking_id): #Удаляем бронь по айди
        response = requests.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers=self._get_headers()
        )
        # В Restful Booker DELETE возвращает 201 — не ошибка!
        if response.status_code != 201:
            response.raise_for_status()
        return response.status_code