import pytest
from django.urls import reverse
import os
import json
import requests
import logging
json_file_path = os.path.join(os.path.dirname(__file__), 'data.json')

logging.basicConfig(level=logging.INFO)

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/kj")



def load_json_file(json_file_path):
  try:
    with open(json_file_path, 'r') as json_file:
      data = json.load(json_file)
      return data
  except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
        return None
  except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} contains invalid JSON.")
        return None   

def test_post_client_plan():
    try:
        data = load_json_file(json_file_path)
        User_details = data[0].get("details")
        if not User_details :
            raise ValueError("User Details not found")
        response = requests.post(BASE_URL  + "/clientAllDetail/" , json=User_details)
        if response.status_code != 201:
                raise Exception(f"POST request failed with status {response.status_code}")
        assert response.status_code == 201 , f"POST request failed with status {response.status_code}"
        print("POST",response.json())    

        response_get = requests.get(BASE_URL + "/clientAllDetail")
        if response.status_code != 201:
                raise Exception(f"GET request failed with status {response.status_code}")
        assert response_get.status_code == 200 , f"GET request failed with status {response_get.status_code}"
        print("GET",response.json())
        retrieved_data = response_get.json()
        assert isinstance(retrieved_data, list), "Expected list of client details"
        client_data = retrieved_data[0]  
        assert client_data['phone'] == User_details['phone'], f"Expected {User_details['phone']} but got {client_data['phone']}"

   
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
    except ValueError as val_err:
        print(f"Value error: {val_err}")
    except AssertionError as assert_err:
        print(f"Assertion error: {assert_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
             





def test_get_client_plan():
    response = requests.get(BASE_URL  + "/plan/1/")
    assert response.status_code == 200 


def test_get_client_address():
    response = requests.get(BASE_URL  + "/address/1/")
    assert response.status_code == 200 



def test_post_diet():
  try:
    data = load_json_file(json_file_path)
    diet =   data[1].get("diet")
    if not diet :
       raise ValueError("Diet not found in json")
    response = requests.post(BASE_URL + "/dietPlan/" , json =diet ) 
    if response.status_code != 201:
        raise Exception(f"POST request failed with status {response.status_code}")
    assert response.status_code == 201   
    client = response.json()["client"]
    date = response.json()["date"]
    response_get = requests.get(BASE_URL + "/client/" + str(client) + "/diet_plan/" + date + "/")
    if  response_get.status_code != 200 :
         raise ValueError("Error occured in GET Diet request")
    if  response_get["date"] != date :
        raise ValueError("Date not matched of diet plan")
  except ValueError as val_err:
        print(f"Value error: {val_err}")
      

# def test_put_note():
#     data = load_json_file(json_file_path)
#     note  = data[0].PUT("note")
#     response = requests.put(BASE_URL + "/note/1/" , json=note )
#     assert response.status_code == 200


# def test_put_note():
#     try:
#         data = load_json_file(json_file_path)
#         if data is None:
#             raise ValueError("Failed to load data from the JSON file.")
#         note = data[2].get("note")
#         if note is None:
#             raise ValueError("No 'note' found in the JSON data.")

#         response = requests.put(BASE_URL + "/note/1/", json={"note": note})
#         assert response.status_code == 200, f"PUT request failed with status {response.status_code}"
#         print("PUT request successful, note updated.")

#     except requests.exceptions.RequestException as req_err:
#         print(f"Request error: {req_err}")
#     except ValueError as val_err:
#         print(f"Value error: {val_err}")
#     except AssertionError as assert_err:
#         print(f"Assertion error: {assert_err}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {str(e)}")


        

