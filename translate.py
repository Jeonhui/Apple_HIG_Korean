import os
import sys
import requests


# test - 주석 해제
import environ
environ.environ()

# translate text with papago API
def translate(text):
    # Header Info
    client_id = os.getenv('X_Naver_Client_Id')
    client_secret = os.getenv('X_Naver_Client_Secret')

    # Post Url
    url = "https://openapi.naver.com/v1/papago/n2mt"

    # Header
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    print(headers)

    # Data
    data = {'source': 'en', 'target': 'ko', 'text': text}

    # Post
    response = requests.post(url, headers=headers, json=data)

    # return response data
    if response.status_code == 200:
        return response.json()['message']['result']['translatedText']
    else:
        return 'error'




text = "An accessible app or game supports accessibility personalizations by design and gives everyone a great user experience, regardless of their capabilities or how they use their devices."
print(translate(text))
