
import requests

url = "http://localhost:5100/api/auth/signup"
data = {
    "name": "SAI SHASHANK",
    "email": "asaishashankallampally@gmail.com",
    "password": "Saisha1211shank@1211"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
