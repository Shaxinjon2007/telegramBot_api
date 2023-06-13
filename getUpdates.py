import requests

TOKEN = '6230054578:AAHrZTfow2U34DALDyyfKrrP0m4FeI6tSj0'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


response = requests.get(url=BASE_URL)
updates=response.json()['result']
print(response.json())
# print each updat
print(updates)
