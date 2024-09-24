import pytest
from django.urls import reverse
import os
import json
import requests
import logging

json_file_path = os.path.join(os.path.dirname(__file__), 'data.json')

logging.basicConfig(level=logging.INFO)


# BASE_URL = "https://panel-django.onrender.com/kj"
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/kj")

with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

def test_post_client_plan():
    person_details = data[0].get("details")
    response = requests.post(BASE_URL  + "/clientAllDetail" , json=person_details)
    print("post data" ,response.json())
    print("POST status code:", response.status_code)
    assert response.status_code == 200 , f"POST request failed with status {response.status_code}"
    # response_get = requests.get(BASE_URL + "/clientAllDetail")
    # assert response_get.status_code == 200 , f"GET request failed with status {response_get.status_code}"
    # print("retieved data" , response_get.json())
    # retrieved_data = response_get.json()
    # assert isinstance(retrieved_data, list), "Expected list of client details"
    # client_data = retrieved_data[0]  
    
    # assert client_data['phone'] == person_details['phone'], f"Expected {person_details['phone']} but got {client_data['phone']}"




# def test_get_client_allDetail():
#     response = requests.get(BASE_URL  + "/clientAllDetail/")
#     assert response.status_code == 200 


# def test_get_client_plan():
#     response = requests.get(BASE_URL  + "/plan/1")
#     assert response.status_code == 200 


# def test_get_client_plan():
#     response = requests.get(BASE_URL  + "/address/1")
#     assert response.status_code == 200 



# def test_post_diet():
#     diet =   data[0].get("diet")
#     response = requests.post(BASE_URL + "/dietPlan" , json =diet ) 
#     assert response.status_code == 200   


# def test_put_note():
#     note  = data[0].get("note")
#     response = requests.put(BASE_URL + "/note/1" , json=note )
#     assert response.status_code == 200





        

