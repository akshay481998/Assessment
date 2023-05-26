import requests
import pandas as pd
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
    pokemons = data.get("pokemon")

    # Define empty lists to store the data.
    ids_list = []
    nums_list = []
    names_list = []
    imgs_list = []
    types_list = []
    height_list = []
    weight_list = []
    candy_list = []
    candy_count_list = []
    eggs_list = []
    spawn_chances_list = []
    avg_spawns_list = []
    spawn_time_list = []
    multipliers_list = []
    weaknesses_list = []
    next_evolutions_list = []
    prev_evolutions_list = []


    logging.info("Extract the required attributes from the data")
    logging.info("We are fetching the ids from the pokemon.")
    for pokemon in pokemons:
        ids = pokemon.get("id")
        try:
            if pd.notnull(ids):
                ids_list.append(int(ids))
            else:
                ids_list.append(None)
        except Exception as e:
                logging.exception(e)


    logging.info("We are fetching the nums from the pokemon.")
    for pokemon in pokemons:
        nums = pokemon.get("num")
        try:
            if pd.notnull(nums):
                nums_list.append(int(nums))
            else:
                nums_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the names from the pokemon.")
    for pokemon in pokemons:
        names = pokemon.get("name")
        try:
            if isinstance(names, str):
                names_list.append(names)
            else:
                names_list.append("")
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the imgs from the pokemon.")
    for pokemon in pokemons:
        imgs = pokemon.get("img")
        try:
            if isinstance(imgs, str):
                imgs_list.append(imgs)
            else:
                imgs_list.append("")
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the types from the pokemon.")
    for pokemon in pokemons:
        types = pokemon.get("type")
        try:
            if isinstance(types, str):
                types_list.append(types)
            else:
                types_list.append("")
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the heights from the pokemon.")
    for pokemon in pokemons:
        heights = pokemon.get("height")
        try:
            if pd.notnull(heights):
                heights = heights.replace(" ", "").rstrip("m")
                height_list.append(float(heights))
            else:
                height_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the weights from the pokemon.")
    for pokemon in pokemons:
        weights = pokemon.get("weight")
        try:
            if pd.notnull(weights):
                weights = weights.replace(" ", "").rstrip("kg")
                weight_list.append(float(weights))
            else:
                weight_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the candy from the pokemon.")
    for pokemon in pokemons:
        candy = pokemon.get("candy")
        try:
            if isinstance(candy, str):
                candy_list.append(candy)
            else:
                candy_list.append("")
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the candy_count from the pokemon.")
    for pokemon in pokemons:
        candy_count = pokemon.get("candy_count")
        try:
            if pd.notnull(candy_count):
                candy_count_list.append(int(candy_count))
            else:
                candy_count_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the eggs from the pokemon.")
    for pokemon in pokemons:
        eggs = pokemon.get("egg")
        try:
            if "km" in eggs:
                eggs = eggs.replace(" ", "").rstrip("km")
                eggs_list.append(int(float(eggs)))
            else:
                eggs_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the spawn_chances from the pokemon.")
    for pokemon in pokemons:
        spawn_chances = pokemon.get("spawn_chance")
        try:
            if pd.notnull(spawn_chances):
                spawn_chances_list.append(float(spawn_chances))
            else:
                spawn_chances_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the avg_spawns from the pokemon.")
    for pokemon in pokemons:
        avg_spawns = pokemon.get("avg_spawns")
        try:
            if pd.notnull(avg_spawns):
                avg_spawns_list.append(int(avg_spawns))
            else:
                avg_spawns_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the spawn_time from the pokemon.")
    for pokemon in pokemons:
        spawn_time = pokemon.get("spawn_time")
        spawn_time = spawn_time.replace(" ", "")
        try:
            if spawn_time == "N/A":
                spawn_time_list.append(pd.to_datetime("00:00").time())
            else:
                spawn_time_list.append(pd.to_datetime(spawn_time).time())
        except Exception as e:
            logging.exception(e)


    logging.info("We are fetching the multipliers from the pokemon.")
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
                elif isinstance(multipliers, str):
                    ele_str = multipliers.strip("[]")
                    m_list.append(int(float(ele_str)))
                    multipliers_list.append(m_list)
            else:
                multipliers_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the weaknesses from the pokemon.")
    for pokemon in pokemons:
        weaknesses = pokemon.get("weaknesses")
        try:
            weaknesses_ele = []  # To store ele in weaknesses.
            if isinstance(weaknesses, list):  # checking type of weaknesses
                for ele in weaknesses:
                    weaknesses_ele.append(str(ele.replace(" ", "")))  # remove extra space
                weaknesses_list.append(weaknesses)  # append list of ele in main list
            elif isinstance(weaknesses, str):
                ele_str = weaknesses.replace("[", "").replace("]", "").replace("'", "")
                ele_list = ele_str.split(",")
                for ele in ele_list:
                    weaknesses_ele.append(ele)
                weaknesses_list.append(weaknesses)
            else:
                weaknesses_list.append([])
        except Exception as e:
            raise e

    logging.info("We are fetching the next_evolutions from the pokemon.")
    for pokemon in pokemons:
        next_evolutions = pokemon.get("next_evolution")
        try:
            if isinstance(next_evolutions, list):
                next_evolutions_list.append(next_evolutions)
            elif isinstance(next_evolutions, str):
                data = next_evolutions.replace("[", "").replace("]", "").replace('"', '')
                next_evolutions = eval('[' + data + ']')
                next_evolutions_list.append(next_evolutions)
            else:
                next_evolutions_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("We are fetching the prev_evolutions from the pokemon.")
    for pokemon in pokemons:
        prev_evolutions = pokemon.get("prev_evolution")
        try:
            if isinstance(prev_evolutions, list):
                prev_evolutions_list.append(prev_evolutions)
            elif isinstance(prev_evolutions, str):
                data = prev_evolutions.replace("[", "").replace("]", "").replace('"', '')
                prev_evolutions = eval('[', + data + ']')
                prev_evolutions_list.append(prev_evolutions)
            else:
                prev_evolutions_list.append(None)
        except Exception as e:
            logging.exception(e)

    logging.info("Create a dictionary with the extracted attributes")
    pokemon_data = {
        "id": ids_list,
        "num": nums_list,
        "name": names_list,
        "img": imgs_list,
        "type": types_list,
        "height": height_list,
        "weight": weight_list,
        "candy": candy_list,
        "candy_count": candy_count_list,
        "egg": eggs_list,
        "spawn_chance": spawn_chances_list,
        "avg_spawns": avg_spawns_list,
        "spawn_time": spawn_time_list,
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