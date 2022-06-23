import requests
from pprint import pprint
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    def get(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()
    def upload(self, file_path: str, filename):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response1 = requests.get(url, headers=headers, params=params)
        response1 = response1.json()

        href = response1.get('href', '')
        response2 = requests.put(href, data=open(filename, 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    pprint(uploader.upload(file_path=path_to_file, filename=''))