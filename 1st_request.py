import requests


url = 'https://pokeapi.co/api/v2/pokemon?limit=5'
searching_pokemon = "bulbasaur"
response = requests.get(f"{url}/{searching_pokemon}")
data = response.json()
pokemon_list = data["results"]
print(data)
def test_pokemon():
    for pokemon in pokemon_list:
        if pokemon["name"] == searching_pokemon:
             assert pokemon["name"] == searching_pokemon
