import requests  # type: ignore
import os


BASE_URL = 'https://swapi.dev/api/'
DATA_FOLDER = 'data'


class APIRequester:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path):
        try:
            url = self.base_url + path
            response = requests.get(url)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f'Возникла ошибка при выполнении запроса: {e}')
            return None


class SWRequester(APIRequester):
    def __init__(self, base_url=BASE_URL):
        super().__init__(base_url)

    def get_sw_categories(self):
        response = self.get('/')
        data = response.json()
        return data.keys()

    def get_sw_info(self, sw_type):
        response = self.get(f'/{sw_type}/')
        return response.text


def save_sw_data():
    requester = SWRequester()
    os.makedirs(DATA_FOLDER, exist_ok=True)
    categories = requester.get_sw_categories()
    for category in categories:
        data = requester.get_sw_info(category)
        filename = f'{DATA_FOLDER}/{category}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)


if __name__ == '__main__':
    save_sw_data()
