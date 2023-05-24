import datetime
import requests
import pandas as pd
import math
import logging

logging.basicConfig(filename="pokemon.log",level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')


def download_data_from_link(link):
    """Function to download data from the provided link"""
    try:
        logging.info("We are downloading the data from given link")
        response = requests.get(link)
        data = response.json()
        return data
    except Exception as e:
        logging.exception(e)


def process_data(data):
    """Function to process the downloaded data and convert it into a DataFrame"""
    pokemons = data["pokemon"]

    logging.info("Extract the required attributes from the data")
    ids_list = []
    logging.info("We are fetching the ids from the pokemon.")
    for pokemon in pokemons:
        ids = pokemon.get("id")
        try:
            if isinstance(ids,str):
                ids_list.append(ids)
            else:
                ids_list.append(0)
        except Exception as e:
                logging.exception(e)


    nums_list = []
    logging.info("We are fetching the numbers from the pokemon")
    for pokemon in pokemons:
        nums = pokemon.get("num")
        try:
            if isinstance(nums,str):
                nums_list.append(nums)
            else:
                nums_list.append(0)
        except Exception as e:
            logging.exception(e)


    names_list = []
    logging.info("We are fetching the names from the pokemon")
    for pokemon in pokemons:
        names = pokemon.get("name")
        try:
            if isinstance(names,str):
                names_list.append(names)
            else:
                names_list.append("No name")
        except Exception as e:
                logging.exception(e)

    imgs_list = []
    logging.info("We are fetching the images from the pokemon")
    for pokemon in pokemons:
        imgs = pokemon.get("img")
        try:
            if isinstance(imgs,str):
                imgs_list.append(imgs)
            else:
                imgs_list.append("No url")
        except Exception as e:
                logging.exception(e)

    types_list = []
    logging.info("We are fetching the types from the pokemon")
    for pokemon in pokemons:
        types = pokemon.get("type")
        try:
            if isinstance(types,str):
                types_list.append(types)
            else:
                types_list.append("No type")
        except Exception as e:
            logging.exception(e)


    heights_list = []
    logging.info("We are fetching the heights from the pokemon")
    for pokemon in pokemons:
        heights = pokemon.get("height")
        try:
            if isinstance(heights,str):
                heights_list.append(float(heights.replace(" ", "").rstrip('m')))
            else:
                heights_list.append(0.0)
        except Exception as e:
                logging.exception(e)


    weights_list = []
    logging.info("We are fetching the weights from the pokemon")
    for pokemon in pokemons:
        weights = pokemon.get("weight")
        try:
            if isinstance(weights,str):
                weights_list.append(float(weights.replace(" ","").rstrip('kg')))
            else:
                weights_list.append(0.0)
        except Exception as e:
            logging.exception(e)


    candies_list = []
    logging.info("We are fetching the candies from the pokemon")
    for pokemon in pokemons:
        candies = pokemon.get("candy")
        try:
            if isinstance(candies,str):
                candies_list.append(candies)
            else:
                candies_list.append("No candy")
        except Exception as e:
            logging.exception(e)


    candy_counts_list = []
    logging.info("We are fetching the candy_counts from the pokemon")
    for pokemon in pokemons:
        candy_counts = pokemon.get("candy_count")
        try:
            if candy_counts is not None and not math.isnan(candy_counts):
                candy_counts_list.append(int(candy_counts))
            else:
                candy_counts_list.append(0)
        except Exception as e:
            logging.exception(e)

    eggs_list = []
    logging.info("We are fetching the eggs from the pokemon")
    for pokemon in pokemons:
        eggs = pokemon.get("egg")
        try:
            if isinstance(eggs, str) and eggs != 'NotinEggs':
                eggs_list.append(float(eggs.replace(" ", "").rstrip('km')))
            else:
                eggs_list.append(None)
        except ValueError:
            eggs_list.append(None)  # Handle the specific ValueError for non-convertible values
        except Exception as e:
            logging.exception(e)

    spawn_chances_list = []
    logging.info("We are fetching the spawn_chances from the pokemon")
    for pokemon in pokemons:
        spawn_chances = pokemon.get("spawn_chance")
        try:
            if isinstance(spawn_chances,str):
                spawn_chances_list.append(float(spawn_chances))
            else:
                spawn_chances_list.append(0.0)
        except Exception as e:
            logging.exception(e)

    avg_spawns_list = []
    logging.info("We are fetching the avg_spawns from the pokemon")
    for pokemon in pokemons:
        avg_spawns = pokemon.get("avg_spawns")
        try:
            if isinstance(avg_spawns,str):
                avg_spawns_list.append(int(avg_spawns))
            else:
                avg_spawns_list.append(0)
        except Exception as e:
            logging.exception(e)


    spawn_times_list = []
    logging.info("We are fetching the spawn_times from the pokemon")
    for pokemon in pokemons:
        spawn_times = pokemon.get("spawn_times")
        try:
            if spawn_times is not None:
                if isinstance(spawn_times, float):
                    spawn_times = str(spawn_times)
                    spawn_times = datetime.datetime.strptime(spawn_times,"%M:%S").time()  # converting spawn_times to time format.
                    spawn_times_list.append(spawn_times)
                elif spawn_times == "nan":
                     spawn_times = "00:00"
                     spawn_times = datetime.datetime.strptime(spawn_times,"%M:%S").time()
                     spawn_times_list.append(spawn_times)
                else:
                    spawn_times = datetime.datetime.strptime(spawn_times, "%M:%S").time()
                    spawn_times_list.append(spawn_times)
        except Exception as e:
            logging.exception(e)


    multipliers_list = []
    logging.info("We are fetching the multipliers from the pokemon")
    for pokemon in pokemons:
        multipliers = pokemon.get("multipliers")
        try:
            if multipliers is not None:
                m_list = []
                if isinstance(multipliers, list):
                    for ele in multipliers:
                        ele_str = str(ele).strip("[]")
                        m_list.append(int(float(ele_str)))
                    multipliers_list.append(m_list)
                elif isinstance(multipliers,str):
                    ele_str = multipliers.strip("[]")
                    m_list.append(int(float(ele_str)))
                    multipliers_list.append(m_list)
                else:
                    multipliers_list.append([])
        except Exception as e:
            logging.exception(e)


    weaknesses_list = []
    logging.info("We are fetching the weaknesses from the pokemon")
    for pokemon in pokemons:
        weaknesses = pokemon.get("weakness")
        try:
            if weaknesses is not None:
                weaknesses = []
                if isinstance(weaknesses,list):
                    for ele in weaknesses:
                        weaknesses.append(ele)
                    weaknesses_list.append(weaknesses)
                else:
                    ele_str = weaknesses.replace("[","").replace("]","").replace("'","")
                    ele_list = ele_str.split(",")
                    for ele in ele_list:
                        weaknesses.append(ele)
                    weaknesses_list.append(weaknesses)
        except Exception as e:
            logging.exception(e)


    next_evolutions_list = []
    logging.info("We are fetching the next_evolutions from the pokemon")
    for pokemon in pokemons:
        next_evolutions = pokemon.get("next_evolution")
        try:
            if next_evolutions is not None:
                if isinstance(next_evolutions,list):
                    next_evolutions_list.append(next_evolutions)
                elif isinstance(next_evolutions,str):
                    data = next_evolutions.replace("[","").replace("]","").replace('"','')
                    next_evolutions = eval('[' + data + ']')
                    next_evolutions_list.append(next_evolutions)
                else:
                    next_evolutions_list.append([])
        except Exception as e:
            logging.info(e)


    prev_evolutions_list = []
    logging.info("We are fetching the prev_evolutions from the pokemon")
    for pokemon in pokemons:
        prev_evolutions = pokemon.get("prev_evolution")
        try:
            if prev_evolutions is not None:
                if isinstance(prev_evolutions,list):
                    prev_evolutions_list.append(prev_evolutions)
                elif isinstance(prev_evolutions,str):
                    data = prev_evolutions.replace("[","").replace("]","").replace('"','')
                    prev_evolutions = eval('[', + data + ']')
                    prev_evolutions_list.append(prev_evolutions)
                else:
                    prev_evolutions_list.append([])
        except Exception as e:
            logging.info(e)


    logging.info("Create a dictionary with the extracted attributes")
    pokemon_data = {
        "id": ids_list,
        "num": nums_list,
        "name": names_list,
        "img": imgs_list,
        "type": types_list,
        "height": heights_list,
        "weight": weights_list,
        "candy": candies_list,
        "candy_count": candy_counts_list,
        "egg": eggs_list,
        "spawn_chance": spawn_chances_list,
        "avg_spawns": avg_spawns_list,
        "spawn_time": spawn_times_list,
        "multipliers": multipliers_list,
        "weaknesses": weaknesses_list,
        "next_evolution": next_evolutions_list,
        "prev_evolution": prev_evolutions_list
    }

    logging.info("Create a DataFrame from the dictionary")
    df = pd.DataFrame(pokemon_data)
    return df


def export_to_excel(df, filename):
    """Function to export DataFrame to Excel format"""
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