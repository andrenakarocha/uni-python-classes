import requests

def get_pokemon_evolution(pokemon_name):
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_evolutions.json"

    headers = {
        "x-rapidapi-key": "7d392f43c2msh37a830b572573cep1f85f7jsnfef0abfe1835",
        "x-rapidapi-host": "pokemon-go1.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)

        pokemon_evolutions = response.json()

        evolutions_dict = {pokemon['pokemon_name']: pokemon['evolutions'][0]['pokemon_name'] for pokemon in pokemon_evolutions}

        if pokemon_name in evolutions_dict:
            return evolutions_dict[pokemon_name]
        else:
            return 'Pokemon not found, try again please!'
    
    except requests.RequestException as e:
        return f"Request Error: {str(e)}"

selected_pokemon = input("Type a pokemon's name to see it's evolution: ")
print(get_pokemon_evolution(selected_pokemon))
