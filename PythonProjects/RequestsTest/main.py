import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '16ab186027ecdd2dd751c64753eb54cd'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_new_poremons = {
    "name": "generate",
    "photo_id": "-1"
}

body_change = {
    "pokemon_id": "305644",
    "name": "kraken",
    "photo_id": "-1"
}

body_pokeball = {
    "pokemon_id": "305644"
}


'''NEW POKEMON'''

result = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_new_poremons)
print(result.text)

'''POKEMON CHANGE'''

result_change = requests.put(url=f'{URL}/pokemons', headers=HEADER,json=body_change)
print(result_change.text)

'''CATCH AT POKEBALL'''

trap = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(trap.text)