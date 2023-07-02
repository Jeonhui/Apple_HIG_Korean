import os
import requests
from AHKError import AHKError
# test - 주석 해제
# import environ
# environ.environ()

class PapagoAPI:
    capacity = 0
    MAX_CAPACITY = 10000
    url = "https://openapi.naver.com/v1/papago/n2mt"

    def __init__(self):
        # header info
        self.client_id = os.getenv('X_NAVER_CLIENT_ID')
        self.client_secret = os.getenv('X_NAVER_CLIENT_SECRET')

    def translate(self, text):
        if self.capacity + len(text) > self.MAX_CAPACITY:
            return AHKError.OverCapacityError
        # Header
        headers = {'X-Naver-Client-Id': self.client_id, 'X-Naver-Client-Secret': self.client_secret}

        # Data
        data = {'source': 'en', 'target': 'ko', 'text': text}

        # Post
        response = requests.post(self.url, headers=headers, json=data)

        # return response data
        if response.status_code == 200:
            return response.json()['message']['result']['translatedText']
        else:
            return AHKError.ResponseError

    def set_capacity(self, capacity):
        self.capacity = capacity
