import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '16ab186027ecdd2dd751c64753eb54cd'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '30474'
TRAINER_NAME = 'Дартанянь'

def test_status():
    status = requests.get(url=f'{URL}/trainers', params={'treiner_id':TRAINER_ID})
    assert status.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', TRAINER_NAME),('id', TRAINER_ID)])
def test_search_trainer(key, value):
    trainer = requests.get(url=f'{URL}/trainers', params={'treiner_id':TRAINER_ID, 'name':TRAINER_NAME})
    assert trainer.json()["data"][0][key] == value



