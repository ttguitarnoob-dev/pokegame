# pokegame

- 
run this code at startup to populate a list of all pokemon names from the api:

pokes = []
NAMES_URL = 'https://pokeapi.co/api/v2/pokemon/?limit=770'
resp = requests.get(URL)
data = resp.json()
for i in data['results']:
    pokes.append(i['name'])

then randomly search the poke database every 10 seconds or so using a random name from the list and then populating a sprite with that data that the player can catch

