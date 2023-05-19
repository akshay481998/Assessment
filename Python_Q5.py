import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup
def download_data_from_link(link):
    response = requests.get(link)
    data = response.json()
    return data

def process_data(data):
    #Let's extract the required attributes in desired datatypes.
    episodes = data["_embedded"]["episodes"]
    ids = [int(episode.get("id")) for episode in episodes]
    urls = [episode.get("url") for episode in episodes]
    names = [episode.get("name") for episode in episodes]
    seasons = [int(episode.get("season")) for episode in episodes]
    numbers = [int(episode.get("number")) for episode in episodes]
    types = [episode.get("type") for episode in episodes]
    runtime = [float(episode.get("runtime")) if episode.get("runtime") else None for episode in episodes]
    ratings = [float(episode.get("rating",{}).get("average")) if episode.get("rating",{}).get("average") else None for episode in episodes]
    summary = [BeautifulSoup(episode.get("summary",""),"html.parser").get_text() for episode in episodes]
    medium_image_links = [episode["image"]["medium"] if episode.get("image") else "" for episode in episodes]
    original_image_links = [episode["image"]["original"] if episode.get("image") else "" for episode in episodes]

    #We need airdate in date formate.
    airdate = []
    for episode in episodes:
        airdate_str = episode.get("airdate")
        if airdate_str:
            try:
                airdates = datetime.datetime.strptime(airdate_str,"%Y-%m-%d").date()
                airdate.append(airdates)
            except ValueError:
                airdate.append(None)
        else:
            airdate.append(None)

    # We need airtime attribute in 12-hour time formate.
    airtime = []
    for episode in episodes:
        airtime_str = episode.get("airtime")
        if airtime_str:
            try:
                airtimes = datetime.datetime.strptime(airtime_str, "%H-%M").strptime("%I:%M %p")
                airtime.append(airtime)
            except ValueError:
                airtime.append(airtime)
        else:
            airtime.append(airtime)

    formatted_data = {
        "id": ids,
        "url": urls,
        "name": names,
        "season": seasons,
        "number": numbers,
        "type": types,
        "airdate": airdate,
        "airtime": airtime,
        "runtime": runtime,
        "average rating": ratings,
        "summary": summary,
        "medium image link": medium_image_links,
        "original image link": original_image_links
    }

    return formatted_data

def create_dataframe(formatted_data):
    df = pd.DataFrame(formatted_data)
    return df

if __name__ == "__main__":
    link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
    data = download_data_from_link(link)
    formatted_data = process_data(data)
    df = create_dataframe(formatted_data)