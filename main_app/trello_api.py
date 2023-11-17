from dotenv import load_dotenv
import os
import requests
board_id = 'Vfa4GNIB'
load_dotenv()
API_KEY = os.getenv('API_KEY')
TOKEN = os.getenv('TOKEN')


def create_trello_card(card_name, list_id, API_KEY, TOKEN, card_description):
    url = 'https://api.trello.com/1/cards'
    query = {
        'idList': list_id,
        'name': card_name,
        'key': API_KEY,
        'token': TOKEN,
        'desc': card_description
    }
    response = requests.post(url, params=query)
    return response.json()


def get_trello_list_ids(board_id, API_KEY, TOKEN):
    url = f'https://api.trello.com/1/boards/{board_id}/lists'
    params = {'key': API_KEY, 'token': TOKEN}
    response = requests.get(url, params=params)

    lists = response.json()
    return {lst['name']: lst['id'] for lst in lists}
