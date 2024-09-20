import requests

# url = "http://127.0.0.1:8000/kj"
url = "https://panel-django.onrender.com/kj/"


def get_test_api(url) :
    try :
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200 :
            print(f"Checked : {url}" )
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: ")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None



def post_test_api(url ,data) :
    try :
        response = requests.post(url , json=data)
        response.raise_for_status()
        if response.status_code == 200 :
            print(f"Checked : {url}" )
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: ")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None


get_api_urls = [
     url + "/clientAllDetail/"  ,
     url + "/client/1/",
     url + "/plan/1/",
     url + "/address/1",
     url + "client/1/diet_plan/2024-08-01/",

]

post_api_urls = [
    { "url" : url + "/clientAllDetail/"  , "data" : 
     {  "name": "ayushi ji ",
        "age": 21,
        "gender": "m",
        "phone": "24238513",
        "email": "9q3u@gmail.com",
        "diet_preference": "Vegetarian",
        "diet_language": "hindi",
       "note": "",
        "address": {
            "city": "gwl",
            "state": "mp",
            "country": "india",
            "zone":"Asia/Kolkata"
        },
        "insights": [
            {
            "height": 5,
            "current_weight": 50,
            "target_weight": 60,
            "height_Unit": "cm",
            "weight_Unit": "kg",
            "persona": "reduce wt"

        }],
        "plan": 
           [ {
                "plan_level": "B",
                "status": "Created",
                "duration": 33,
                "start_time": "2024-08-03",
                "end_time": "2024-09-17"
            }]} 
    } , 
   
    {"url" : url + "/dietPlan/" , "data" : {
    "day1" : {
    "meal1": ["lemon"],
    "meal2": ["chekko"],
    "meal3": ["aloo"],
    "meal4": ["fff"],
    "meal5": ["lalu"],
    "meal6": [],
    "meal7": []
  },
    "day2" :{
    "meal1": ["aloo"],
    "meal2": [],
    "meal3": [],
    "meal4": [],
    "meal5": [],
    "meal6": [],
    "meal7": []
  },
    "day3" : {
    "meal1": [],
    "meal2": [],
    "meal3": [],
    "meal4": [],
    "meal5": [],
    "meal6": [],
    "meal7": []
  },
    "day4" : {
    "meal1": [],
    "meal2": [],
    "meal3": [],
    "meal4": [],
    "meal5": [],
    "meal6": [],
    "meal7": []
  },
    "day5" : {
    "meal1": [],
    "meal2": [],
    "meal3": [],
    "meal4": [],
    "meal5": [],
    "meal6": [],
    "meal7": []
  },
    "day6" :{
    "meal1": [],
    "meal2": [],
    "meal3": [],
    "meal4": [],
    "meal5": [],
    "meal6": [],
    "meal7": []
  },
    "day7" :{
    "meal1": [],
    "meal2": [],
    "meal3": [],
    "meal4": [],
    "meal5": [],
    "meal6": [],
    "meal7": []
  },
  "note":"",
  "meal_Time":{},
  "date":"2024-08-02",
  "client":1
}}
   
 
]


for url in get_api_urls : 
    get_test_api(url)


# for api_info in post_api_urls:
#     post_test_api(url = api_info["url"] , data = api_info["data"])


  
