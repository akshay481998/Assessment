import requests
import pandas as pd

# Function to download data from the provided link
def download_data_from_link(link):
    response = requests.get(link)
    data = response.json()
    return data

# Function to process the downloaded data and convert it into a DataFrame
def process_data(data):
    pokemons = data["pokemon"]

    # Extract the required attributes from the data
    ids = [int(pokemon.get("id")) for pokemon in pokemons]
    nums = [int(pokemon.get("num")) for pokemon in pokemons]
    names = [pokemon["name"] for pokemon in pokemons]
    imgs = [pokemon["img"] for pokemon in pokemons]
    types = [pokemon["type"] for pokemon in pokemons]
    heights = [float(pokemon.get("height")) for pokemon in pokemons]
    weights = [float(pokemon.get("weight")) for pokemon in pokemons]
    candies = [pokemon.get("candy") for pokemon in pokemons]
    candy_counts = [int(pokemon.get("candy_count")) for pokemon in pokemons]
    eggs = [float(pokemon.get("egg", 0)) for pokemon in pokemons]
    spawn_chances = [float(pokemon.get("spawn_chance", 0)) for pokemon in pokemons]
    avg_spawns = [int(pokemon.get("avg_spawns", 0)) for pokemon in pokemons]
    spawn_times = [pokemon.get("spawn_time") for pokemon in pokemons]
    multipliers = [list(map(float, pokemon.get("multipliers", []))) for pokemon in pokemons]
    weaknesses = [pokemon.get("weaknesses") for pokemon in pokemons]
    next_evolutions = [pokemon.get("next_evolution", []) for pokemon in pokemons]
    prev_evolutions = [pokemon.get("prev_evolution", []) for pokemon in pokemons]
    # Create a dictionary with the extracted attributes
    pokemon_data = {
        "id": ids,
        "num": nums,
        "name": names,
        "img": imgs,
        "type": types,
        "height": heights,
        "weight": weights,
        "candy": candies,
        "candy_count": candy_counts,
        "egg": eggs,
        "spawn_chance": spawn_chances,
        "avg_spawns": avg_spawns,
        "spawn_time": spawn_times,
        "multipliers": multipliers,
        "weaknesses": weaknesses,
        "next_evolution": next_evolutions,
        "prev_evolution": prev_evolutions
    }

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(pokemon_data)
    return df

# Function to export DataFrame to Excel format
def export_to_excel(df, filename):
    df.to_excel(filename, index=False)


if __name__ == "__main__":
    # the link to download the data
    link = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

    # Download the data from the link
    data = download_data_from_link(link)

    # Process the data and convert it into a DataFrame
    df = process_data(data)

    # Define the filename for the Excel file
    filename = "pokemon_data.xlsx"

    # Export the DataFrame to Excel format
    export_to_excel(df, filename)