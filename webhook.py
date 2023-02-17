import requests
import os

url = "https://bekzod1997.pythonanywhere.com/api"

TOKEN = os.environ["TOKEN"]

payload = {
    "url": url
}

response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook', params=payload)
print(response.status_code)