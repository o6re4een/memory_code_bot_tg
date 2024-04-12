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


token = authorize_user(EMAIL, PASSWORD)

def search_individual_page(token):
    pages_sp_url = "https://mc.dev.rand.agency/api/cabinet/individual-pages"
    print("Search, pages", token)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(pages_sp_url, headers=headers)
    page_info =response.json()
    # page_info: Page = Page(**response.json()[0])
    print(page_info)
    print(page_info, type(page_info))

search_individual_page(token)




def update_page():
    pass



