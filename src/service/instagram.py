import requests
import os

from dotenv import *
from icecream import ic
from src.utils.file import File

class Instagram:
    def __init__(self) -> None:
        load_dotenv()
        self.__file = File()
        self.__COOKIES = os.getenv('COOKIE')

        self.__main_api = 'https://www.instagram.com/api/v1/feed/user/jkt48.freya/username/?count=150'
        self.__second_api = 'https://www.instagram.com/api/v1/feed/user/9884975657/?count=12&max_id=3223585292288501499_9884975657'

        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': str(self.__COOKIES),
            'Dpr': '2',
            'Referer': 'https://www.instagram.com/jkt48.freya/',
            'Sec-Ch-Prefers-Color-Scheme': 'dark',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Full-Version-List': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Google Chrome";v="120.0.6099.130"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Viewport-Width': '1920',
            'X-Asbd-Id': '129477',
            'X-Csrftoken': 'VqFUdHhunrwbNuPNn3UgjYlWYMPHrnwD',
            'X-Ig-App-Id': '936619743392459',
            'X-Ig-Www-Claim': 'hmac.AR3HkuG7h3TIwMO3PJ6UKkzx9pH9Qm5gwQvd0oQNocS8xwqH',
            'X-Requested-With': 'XMLHttpRequest'
        }


    def main(self):
        # response = requests.get(url=self.__api, headers=self.headers)
        response = requests.get(url='https://www.instagram.com/api/v1/feed/user/9884975657/?count=12&max_id=3223585292288501499_9884975657', headers=self.headers)
        self.__file.write_json(path='private/response3.json', content=response.json())

        ic(response)

        # file = self.__file.read_json('private/response.json')

        # ic(len(file['items']))
        