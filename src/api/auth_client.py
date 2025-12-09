import requests
from config.settings import BASE_URL

class AuthClient:
    def __init__(self):
        self.base_url = BASE_URL
    
    def create_token(self, username="admin", password="password123"):
        payload = {"username": username, "password": password}
        response = requests.post(
            f'{self.base_url}/auth',
           json=payload 
        )
        response.raise_for_status() #вызываем исключение HTTPError, если запрос вернул неудачный код состояния HTTP
        return response.json()['token'] #Возвращаем токен