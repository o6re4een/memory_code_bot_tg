import requests
import ast
import json
import os
from dotenv import load_dotenv

load_dotenv()

FOLDER_ID = os.getenv('FOLDER_ID')
API_KEY = os.getenv('API_KEY')



headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {API_KEY}"
}
url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
def get_biography(arrdata):
    allname=arrdata[2].split(" ", 2)
    name=allname[1]
    last_name=allname[0]
    age=arrdata[3]
    placebirth=arrdata[4]
    prof=arrdata[5]
    freetim=arrdata[6]
    hobby=arrdata[7]
    relegion=arrdata[8]
    values=arrdata[9]
    goodrel=arrdata[10]
    personality=arrdata[11]
    specmoments=arrdata[12]
    prompt = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
        {
        "role": "system",
        "text": f"Ты — опытный составитель биографии. Напиши биографию с учётом полученных данных. Имя-{name}, фамилия - {last_name}, ему было: {age}, когда он покинул наш мир , он родился в: {placebirth}, работал: {prof}, в свободное время он: {freetim}, его хобби: {hobby}, он придерживался религии: {relegion} и следующих ценностей: {values}, на вопрос был ли он семьянином он бы ответил: {goodrel},его характер: {personality},ценные моменты или истории:{specmoments}."
        },
        {
        "role": "user",
        "text": "Вид текста: пост на страницу с описанием человека. Тема: Биография человека по представленным данным."
        }
        ]
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.text
    print(result)