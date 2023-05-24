import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import logging

logging.basicConfig(filename="episodes.log", level=logging.INFO, format="%(levelname)s %(asctime)s %(name)s %(message)s")

def download_data_from_link(link):
    """Function to download data from the provided link"""
    try:
        logging.info("We are downloading the data from provided link")
        response = requests.get(link)
        data = response.json()
        return data
    except Exception as e:
        logging.exception(e)

def process_data(data):
    """Function to process the data attributes in desired data types"""

    episodes = data["_embedded"]["episodes"]

    # Let's define the empty lists to store the data.
    ids_list = []
    url_list = []
    names_list = []
    season_list = []
    nums_list = []
    type_list = []
    airdates_list = []
    airtimes_list = []
    runtimes_list = []
    average_rating_list = []
    summary_list = []
    medium_img_link_list = []
    original_img_link_list = []

    logging.info("Let's extract the required attributes in desired datatypes.")
    for episode in episodes:
        ids = episode.get("id", 0)
        try:
            logging.info("We are fetching the ids from the episode data")
            if isinstance(ids, str) or isinstance(ids, int):
                ids_list.append(int(ids))
            else:
                ids_list.append(0)
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        url = episode.get("url")
        try:
            logging.info("We are fetching the url from the episode data")
            if isinstance(url, str):
                url_list.append(url)
            else:
                url_list.append("")
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        names = episode.get('name')
        try:
            logging.info("We are fetching the names from the episode data")
            if isinstance(names, str):
                names_list.append(names)
            else:
                names_list.append("")
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        seasons = episode.get("season")
        try:
            logging.info("We are fetching the seasons from the episode data")
            if isinstance(seasons, int) or isinstance(seasons, str):
                season_list.append(int(seasons))
            else:
                season_list.append(0)
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        nums = episode.get("number")
        try:
            logging.info("We are fetching the nums from the episode data")
            if isinstance(nums, str) or isinstance(nums, int):
                nums_list.append(nums)
            else:
                nums_list.append(0)
        except Exception as e:
            logging.info(e)

    for episode in episodes:
        types = episode.get("type")
        try:
            logging.info("We are fetching the types from the episode data")
            if isinstance(types, str):
                type_list.append(types)
            else:
                type_list.append("")
        except Exception as e:
            logging.info(e)

    for episode in episodes:
        airdates = episode.get("airdate")
        try:
            logging.info("We are fetching the airdates from the episode data")
            if airdates is not None:
                if isinstance(airdates, str):
                    airdates = pd.to_datetime(airdates).date()
                    airdates_list.append(airdates)
            else:
                airdates_list.append(None)
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        airtimes = episode.get("airtime")
        try:
            logging.info("We are fetching the airtimes from the episode data")
            if pd.notnull(airtimes):
                airtimes = str(airtimes) + ":00"
                airtimes = pd.to_datetime(airtimes, format="%H:%M:%S").time()
            else:
                airtimes = pd.to_datetime("21:00:00", format="%H:%M:%S").time()
            formatted_airtime = airtimes.strftime("%I:%M %p")
            airtimes_list.append(formatted_airtime)
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        runtimes = episode.get("runtime")
        try:
            logging.info("We are fetching the runtimes from the episode data")
            if pd.notnull(runtimes):
                runtimes_list.append(float(runtimes))
            else:
                runtimes_list.append(0)
        except Exception as e:
            logging.info(e)

    for episode in episodes:
        average_rating = episode.get("rating").get("average")
        try:
            logging.info("We are fetching the average_rating from the episode data")
            if pd.notnull(average_rating):
                average_rating_list.append(float(average_rating))
            else:
                average_rating_list.append(0)
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        summary = str(episode.get("summary"))
        try:
            logging.info("We are fetching the summary from the episode data")
            if pd.notnull(summary):
                summary = BeautifulSoup(summary, "html.parser").get_text()
                summary_list.append(summary)
            else:
                summary_list.append("")
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        medium_img_link = episode.get("image").get("medium")
        try:
            logging.info("We are fetching the medium_img_link from the episode data")
            if pd.notnull(medium_img_link):
                medium_img_link = str(medium_img_link)
                medium_img_link_list.append(medium_img_link)
            else:
                medium_img_link_list.append("")
        except Exception as e:
            logging.exception(e)

    for episode in episodes:
        original_img_link = episode.get("image").get("original")
        try:
            logging.info("We are fetching the original_img_link from the episode data")
            if pd.notnull(original_img_link):
                original_img_link = str(original_img_link)
                original_img_link_list.append(original_img_link)
            else:
                original_img_link_list.append("")
        except Exception as e:
            logging.exception(e)

    logging.info("Create a dictionary with the extracted attributes")
    formatted_data = {
        "id": ids_list,
        "url": url_list,
        "name": names_list,
        "season": season_list,
        "number": nums_list,
        "type": type_list,
        "airdate": airdates_list,
        "airtime": airtimes_list,
        "runtime": runtimes_list,
        "average rating": average_rating_list,
        "summary": summary_list,
        "medium image link": medium_img_link_list,
        "original image link": original_img_link_list
    }

    return formatted_data

def create_dataframe(formatted_data):
    """It will create DataFarme with given dictionary"""
    df = pd.DataFrame(formatted_data)
    return df

def export_to_csv(df,filename):
    df.to_csv(filename,index=False)

if __name__ == "__main__":
    link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
    data = download_data_from_link(link)
    formatted_data = process_data(data)
    df = create_dataframe(formatted_data)
    filename = "formatted_data.csv"
    export_to_csv(df,filename)