import pytest
from rest_framework import status
# from django.urls import reverse
import os
import requests


# BASE_URL = "https://panel-django.onrender.com/kj"

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/kj")


def test_get_client_allDetail():
    response = requests.get(BASE_URL  + "/clientAllDetail/")
    assert response.status_code == 200 


# def test_get_client_plan():
#     response = requests.get(BASE_URL  + "/plan/1")
#     assert response.status_code == 200 


# def test_get_client_plan():
#     response = requests.get(BASE_URL  + "/address/1")
#     assert response.status_code == 200 


# def test_post_client_plan():
#     data =   {  "name": "lhyati ji ",
#         "age": 21,
#         "gender": "m",
#         "phone": "2423991513",
#         "email": "ayu112@gmail.com",
#         "diet_preference": "Vegetarian",
#         "diet_language": "hindi",
#        "note": "",
#         "address": {
#             "city": "gwl",
#             "state": "mp",
#             "country": "india",
#             "zone":"Asia/Kolkata"
#         },
#         "insights": [
#             {
#             "height": 5,
#             "current_weight": 50,
#             "target_weight": 60,
#             "height_Unit": "cm",
#             "weight_Unit": "kg",
#             "persona": "reduce wt"

#         }],
#         "plan": 
#            [ {
#                 "plan_level": "B",
#                 "status": "Created",
#                 "duration": 33,
#                 "start_time": "2024-08-23",
#                 "end_time": "2024-12-23"
#             }]} 
#     response = requests.post(BASE_URL  + "/clientAllDetail" , json=data)
#     assert response.status_code == 200


# def test_post_diet():
#     data =    { "day1" : {
#     "meal1": ["lemon"],
#     "meal2": ["chekko"],
#     "meal3": ["aloo"],
#     "meal4": ["fff"],
#     "meal5": ["lalu"],
#     "meal6": [],
#     "meal7": []
#   },
#     "day2" :{
#     "meal1": ["aloo"],
#     "meal2": ["rice"],
#     "meal3": [],
#     "meal4": [],
#     "meal5": [],
#     "meal6": [],
#     "meal7": []
#   },
#     "day3" : {
#     "meal1": [],
#     "meal2": [],
#     "meal3": [],
#     "meal4": [],
#     "meal5": [],
#     "meal6": [],
#     "meal7": []
#   },
#     "day4" : {
#     "meal1": [],
#     "meal2": [],
#     "meal3": [],
#     "meal4": [],
#     "meal5": [],
#     "meal6": [],
#     "meal7": []
#   },
#     "day5" : {
#     "meal1": [],
#     "meal2": [],
#     "meal3": [],
#     "meal4": [],
#     "meal5": [],
#     "meal6": [],
#     "meal7": []
#   },
#     "day6" :{
#     "meal1": [],
#     "meal2": [],
#     "meal3": [],
#     "meal4": [],
#     "meal5": [],
#     "meal6": [],
#     "meal7": []
#   },
#     "day7" :{
#     "meal1": [],
#     "meal2": [],
#     "meal3": [],
#     "meal4": [],
#     "meal5": [],
#     "meal6": [],
#     "meal7": []
#   },
#   "note":"",
#   "meal_Time":{},
#   "date":"2024-08-05",
#   "client":2
# }
#     response = requests.post(BASE_URL + "/dietPlan" , json =data ) 
#     assert response.status_code == 200   


# def test_put_note():
#     data  = {
#         "note" : "This note is to be updated"
#     }
#     response = requests.put(BASE_URL + "/note/1" , json=data )
#     assert response.status_code == 200





        

