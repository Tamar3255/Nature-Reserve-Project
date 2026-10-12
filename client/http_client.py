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



def regist_a_new_user(username,password):
    params = [{"username":username,"password": password}]
    try:
        response = requests.post(f"{SERVER_URL}/users/register", json=params)
        if response == True:
            print("User successfully added")
    except requests.exceptions.RequestException as exc:
            return {"error": exc}

def access_approval(username, password):
        params = [{"username": username, "password": password}]
        try:
            response = requests.get(f"{SERVER_URL}/users/register", json=params)
            return response
        except requests.exceptions.RequestException as exc:
            return {"error": exc}


def update_treatment(treatment):
    params = treatment
    try:
        response = requests.post(f"{SERVER_URL}/treatments", json=params)
        if response == True:
            print("The treatment update was successfully completed ")
    except requests.exceptions.RequestException as exc:
            return {"error": exc}


    



