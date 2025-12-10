import requests  # type: ignore
import os


class APIRequester:

    def __init__(self):
        self.base_url = 'https://swapi.dev/api/'

    def get(self, path):
        try:
            url = self.base_url + path
            response = requests.get(url)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f'При запросе возникла ошибка{e}')
            return None


class SWRequester(APIRequester):
    def get_sw_categories(self):
        response = self.get('/')
        data = response.json()
        return list(data.keys())

    def get_sw_info(self, sw_type):
        response = self.get(f'/{sw_type}')
        return response.text


def save_sw_data():
    requester = SWRequester()
    os.makedirs('data', exist_ok=True)
    categories = requester.get_sw_categories()
    for category in categories:
        data = requester.get_sw_info(category)
        filename = f'data/{category}.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)


if __name__ == '__main__':
    save_sw_data()
