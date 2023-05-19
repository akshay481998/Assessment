import requests
import pandas as pd

# Function to download data from the provided link
def download_data_from_link(link):
    response = requests.get(link)
    data = response.json()
    return data

# Function to process the downloaded data and convert it into a DataFrame
def process_data(data):
    # Extract the required attributes from the data
    pokemon_list = data["pokemon"]

    # Initialize empty lists to store the attributes
    ids = []
    nums = []
    names = []
    imgs = []
    types = []
    heights = []
    weights = []
    candies = []
    candy_counts = []
    eggs = []
    spawn_chances = []
    avg_spawns = []
    spawn_times = []
    multipliers = []
    weaknesses = []
    next_evolutions = []
    prev_evolutions = []

    # Iterate over each Pokemon in the list and extract the attributes
    for pokemon in pokemon_list:
        ids.append(pokemon.get("id"))
        nums.append(pokemon.get("num"))
        names.append(pokemon.get("name"))
        imgs.append(pokemon.get("img"))
        types.append(pokemon.get("type"))
        heights.append(pokemon.get("height"))
        weights.append(pokemon.get("weight"))
        candies.append(pokemon.get("candy"))
        candy_counts.append(pokemon.get("candy_count"))
        eggs.append(pokemon.get("egg"))
        spawn_chances.append(pokemon.get("spawn_chance"))
        avg_spawns.append(pokemon.get("avg_spawns"))
        spawn_times.append(pokemon.get("spawn_time"))
        multipliers.append(pokemon.get("multipliers"))
        weaknesses.append(pokemon.get("weaknesses"))
        next_evolutions.append(pokemon.get("next_evolution"))
        prev_evolutions.append(pokemon.get("prev_evolution", []))  # We need to use empty list as default value if key is missing

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