# Перед использование request, необходимо установить библиотекуц request

import requests
from .telegramToken import token, chat_id

def sendTelegram(text = 'Test'):
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text' : text,
    })

# sendTelegram()