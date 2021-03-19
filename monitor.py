#!/usr/bin/python3

import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('settings.ini')

bot_token = config['telegram']['bot_token']
chat_id = config['telegram']['chat_id']

def send_message(message):
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message
    response = requests.get(url)
    return response.json()

def check_server(url):
  try:
    response = requests.get(url, timeout=0.5)
    return response.status_code == 200
  except requests.exceptions.Timeout:
    return False

state_json = 'state.json'
url = 'https://343max.de/'

try:
  with open(state_json) as json_file:
    last_reachable = json.load(json_file)
except FileNotFoundError:
  last_reachable = False
except json.decoder.JSONDecodeError:
  last_reachable = False

current_reachable = check_server(url)

if last_reachable != current_reachable:
  if current_reachable == True:
    send_message('{url} is reachable again'.format(url=url))
  else:
    send_message('{url} is not reachable'.format(url=url))

  with open(state_json, 'w') as json_file:
    json.dump(current_reachable, json_file)
