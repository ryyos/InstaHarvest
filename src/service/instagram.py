import requests
import os

from dotenv import *
from icecream import ic
from datetime import datetime
from time import time

from src.utils.file import File

class Instagram:
    def __init__(self) -> {}:
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


    def extract_data(self, document: dict, search_key: str):

        results = {
            "crawling_time": str(datetime.now()),
            "crawling_time_epoch": int(time()),
            "search_key": search_key,
            "status": document["status"],
            "user": {
                "username": document["user"]["username"],
                "full_name": document["user"]["full_name"],
                "is_private": document["user"]["is_private"],
                "is_verified": document["user"]["is_verified"],
                "profile_pic_id": document["user"]["profile_pic_id"],
                "profile_pic_url": document["user"]["profile_pic_url"],
                "contents": [
                    {
                        "taken_at": content.get("taken_at"),
                        "id": content.get("id"),
                        "commerciality_status": content.get("commerciality_status", None),
                        "explore_hide_comments": content.get("explore_hide_comments", None),
                        "is_quiet_post": content.get("is_quiet_post", None),
                        "mezql_token": content.get("mezql_token", None),
                        "tags": content.get("usertags", {}).get("in", [])[:1],
                        "photo_of_you": content.get("photo_of_you", None),
                        "has_liked": content.get("has_liked", None),
                        "has_privately_liked": content.get("has_privately_liked", None),
                        "like_count": content.get("like_count", None),
                        "can_viewer_reshare": content.get("can_viewer_reshare", None),
                        "video_subtitles": content.get("video_subtitles_uri", None),
                        "captions": content.get("caption", {}).get("text", None),
                        "play_count": content.get("play_count", None),
                        "medias": {
                            "images": content.get("image_versions2", {}).get("candidates", None),
                            "videos": content.get("video_versions", None),
                            "video_durations": content.get("video_duration", None),
                            "audio": {
                                "music_info": content.get("clips_metadata", {}).get("music_info", None),
                                "audio_type": content.get("clips_metadata", {}).get("audio_type", None),
                                "url": content.get("clips_metadata", {}).get("original_sound_info", {}).get("progressive_download_url", None),
                                "should_mute_audio": content.get("clips_metadata", {}).get("original_sound_info", {}).get("should_mute_audio", None)
                            }
                        }
                            
                    } for content in document["items"]
                ]
            }
        }

        return results


    def main(self):
        # response = requests.get(url=self.__api, headers=self.headers)
        # response = requests.get(url='https://www.instagram.com/api/v1/feed/user/9884975657/?count=12&max_id=3223585292288501499_9884975657', headers=self.headers)
        # ic(response)
        # ic(response.text)
        # self.__file.write_json(path='private/response3.json', content=response.json())


        file = self.__file.read_json('private/response.json')
        results = self.extract_data(document=file, search_key="freya")
        self.__file.write_json(path='private/results.json', content=results)

        # ic(len(file['items']))
        