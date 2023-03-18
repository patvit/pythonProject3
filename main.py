
import json
from pprint import pprint
#from ya_disk import YandexDisk
import requests
import os





#=======задача 1============
#
# url = "https://akabab.github.io/superhero-api/api//all.json"
# resp = requests.get(url)
# data = resp.json()
# Heros = ['Hulk','Captain America','Thanos']
# max = 0
# name =''
# for hero in data:
#     if hero['name'] in Heros:
#         if max < hero['powerstats']['intelligence']:
#             max = hero['powerstats']['intelligence']
#             name = hero['name']
#
# print(f"Самый умный герой { name} c интеллектом {max}")


#=======задача 2============

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    # def _get_upload_link(self, disk_file_path):
    #
    #
    #     upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': 'OAuth {}'.format(self.token)
    #     }
    #     params = {'path': disk_file_path, 'overwrite': 'true'}
    #     response = requests.get(upload_url, headers=headers, params=params)
    #     pprint(response.json())
    #     data = response.json()
    #     href = data.get('href')
    #     return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать

        headers = {
            'Content-Type':'application/json',
            'Authorization':'OAuth {}'.format(self.token)
        }

        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(files_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        response = requests.put(href, data=open('1.txt', 'rb'))

    def get_files_list(self):
        headers = {
            'Content-Type':'application/json',
            'Authorization':'OAuth {}'.format(self.token)
        }
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        response = requests.get(files_url, headers=headers)
        data = response.json()
        return response.json()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '1.txt'
    token = ''
    uploader = YaUploader(token)
    # data = uploader.get_files_list()
    # for item in data['items']:
    #     print(item['mime_type'])

    result = uploader.upload(path_to_file)
