import requests

TOKEN = '6230054578:AAHrZTfow2U34DALDyyfKrrP0m4FeI6tSj0'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'


response = requests.get(url=BASE_URL)
if response.status_code == 200:
    info = response.json()
    print(info)