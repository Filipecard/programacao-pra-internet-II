import requests

pokemon = 'pikachu'
url = 'https://pokeapi.co/api/v2/pokemon/{name}'
url = url.format(name = pokemon)
response = requests.get(url).json()

print('Pokemon:',(response['species']['name']).upper())
print('Type:',(response['types'][0]['type']['name'].upper()))
print('Status: HP: {} ,Attack: {} , Defense: {}, Speed: {}'.format(response['stats'][0]['base_stat'],\
    response['stats'][1]['base_stat'],response['stats'][2]['base_stat'],\
        response['stats'][5]['base_stat']))


