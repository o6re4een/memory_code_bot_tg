import requests
import ast
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# from data_sp import Page
# from cfg import EMAIL, PASSWORD


def authorize_user(email, password): 
    auth_url = "https://mc.dev.rand.agency/api/v1/get-access-token"
    headers = {"Accept": "application/json", "Content-Type": "application/json;charset=UTF-8"}
    data = {
        "email": email,
        "password": password,
        "device": "bot-v0.0.1"
    }
    response = requests.post(auth_url, headers=headers, json=data)
    
    access_token = response.text
    access_token = ast.literal_eval(access_token)["access_token"]

    return access_token




def search_individual_page(token):
    pages_sp_url = "https://mc.dev.rand.agency/api/cabinet/individual-pages"
    print("Search, pages", token)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(pages_sp_url, headers=headers)
    page_info =response.json()[1]
    # page_info: Page = Page(**response.json()[0])
    
    return page_info




# Возвращает ссылку на страрицу с биографией 
# 
def update_page(data, token, page_id, slug):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {token}",
    }
    print("Page update", data, token, slug, f"https://mc.dev.rand.agency/api/page/{slug}")
    url = f"https://mc.dev.rand.agency/api/page/{slug}"
    test_data = {
        "id": page_id,
        
        "name": "Иванов Иван Иванович",
        "start": {
            "day": "02",
            "month": "01",
            "year": 1700
        },
        "end": {
            "day": "03",
            "month": "01",
            "year": 2024
        },
        "biographies": [
    {
     
      "title": "1 часть ЗАГОЛОВОК ВСТУПЛЕНИЯ",
      "description": "ТЕКСТ ВСТУПЛЕНИЯ",
      "page_id": 148,
      "created_at": "2023-12-28T07:17:13.000000Z",
      "updated_at": "2023-12-28T07:17:13.000000Z",
      "order": 1,
      "checked": True,
      "photos": [
      ],
      "media": []
    },
    {
     
      "title": "ЗАГОЛОВОК 2 ЧАСТИ",
      "description": "ТЕКСТ 2 ЧАСТИ",
      "page_id": page_id,
      "created_at": "2023-12-28T07:17:13.000000Z",
      "updated_at": "2023-12-28T07:17:13.000000Z",
      "order": 2,
      "checked": True,
      "photos": [],
      "media": []
    },
    {
      
      "title": "ЗАГОЛОВОК 3 ЧАСТИ",
      "description": "ТЕКСТ 3 ЧАСТИ",
      "page_id": page_id,
      "created_at": "2023-12-28T07:17:13.000000Z",
      "updated_at": "2023-12-28T07:17:13.000000Z",
      "order": 3,
      "checked": True,
      "photos": [],
      "media": []
    },
    {
      
      "title": "Zakluchenie",
      "description": "ТЕКСТ ЗАКЛЮЧЕНИЯ",
      "page_id": page_id,
      "created_at": "2023-12-28T07:17:13.000000Z",
      "updated_at": "2023-12-28T07:17:13.000000Z",
      "order": 4,
      "checked": True,
      "photos": [],
      "media": []
    }
    ],
        "epitaph": "КРАТКАЯ ЭПИТАФИЯ",
        "author_epitaph": "АВТОР ЭПИТАФИИ",
        "page_type_id": "1"
    }   
    try :
        response = requests.put(url, headers=headers, json=test_data)
        print("Page update status: ", response.status_code)
        return f'https://mc.dev.rand.agency/api/page/{slug}'
    except Exception as ex:
        print("Page update status: ", response.status_code)
        print(ex)
        return None
    
    
    # print(response.json())
    

# token = authorize_user(EMAIL, PASSWORD)
# founded_page = search_individual_page(token)
# update_page(founded_page["name"], token, founded_page["id"], founded_page["slug"])
