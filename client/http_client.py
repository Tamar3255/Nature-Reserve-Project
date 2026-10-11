from dotenv import load_dotenv
import os
import requests
load_dotenv()

SERVER_URL = os.getenv("SERVER_URL")


def request_last_reserve(search_type, search_value):
    print(search_type,search_value)
    params = {"id": search_value} if search_type == "id" else {"collar code": search_value}
    print(params)
    try:
        response = requests.get(f"{SERVER_URL}/animals/last-reserve", params=params)
        data = response.json()
        print(data)
        return response
    except requests.exceptions.RequestException as exc:
            return {"error": exc}

def checking_username(name):
    params = {"username": name}
    try:
        response = requests.get(f"{SERVER_URL}/register/username", params=params)
        return response
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Unable to connect to the server. Ensure the server is active and the address is correct.")

def regist_a_new_user(username,password):
    params = [{"username":username,"password": password}]
    response = requests.get(f"{SERVER_URL}/register/last-reserve", params=params)
    



