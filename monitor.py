#!/usr/bin/python3

import requests
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

bot_token = config['telegram']['bot_token']
chat_id = config['telegram']['chat_id']

def send_message(message):
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message
    response = requests.get(url)
    return response.json()

response = send_message('Hello!')
print(response)