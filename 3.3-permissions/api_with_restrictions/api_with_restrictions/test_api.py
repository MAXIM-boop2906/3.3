
import requests

# ВСТАВЬ СЮДА СВОЙ ТОКЕН ИЗ ШАГА 1
TOKEN = "c5f5a15d6b0c3a9a5f45c3a5fb531405079997ba"
URL = "http://127.0.0.1:8000/api/advertisements/"

print("=== Создание объявления ===")
response = requests.post(
    URL,
    json={"title": "Продаю ноутбук", "description": "В идеальном состоянии"},
    headers={"Authorization": f"Token {TOKEN}"}
)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

print("\n=== Просмотр списка объявлений ===")
response = requests.get(URL)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")