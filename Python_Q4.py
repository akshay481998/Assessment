import requests
import pandas as pd

def download_data_from_link(link):
    response = requests.get(link)
    data = response.json()
    return data

def process_data(data):
    #Let's extract all the attributes from the data
    meteorite_list = data

    #Define the lists to store all the data points
    names = []
    ids = []
    nametypes = []
    recclasses = []
    masses = []
    years = []
    reclats = []
    reclongs = []
    coordinates = []

    #Iterate over each meteorite in the list and extarct the attributes.
    for meteorite in meteorite_list:
        names.append(meteorite.get("name"))
        ids.append(meteorite.get("id"))
        nametypes.append((meteorite.get("nametype")))
        recclasses.append(meteorite.get("recclass"))
        masses.append(float(meteorite.get("mass", 0)))
        try:
            years.append(pd.to_datetime(meteorite.get("year")))
        except (ValueError, pd.errors.OutOfBoundsDatetime):
            years.append(pd.to_datetime("1900-01-01"))
        reclats.append(float(meteorite.get("reclat",0)))
        reclongs.append(float(meteorite.get("reclong",0)))
        coordinates.append([float(meteorite.get("reclong",0)),float(meteorite.get("reclat",0))])
        #A list containing longitude and latitude coordinates is constructed and appended to the coordinates list.

    #Create a dictionary from extracted attributes.
    meteorite_data = {
        "Name of Earth Meteorite": names,
        "id": ids,
        "Meteorites": nametypes,
        "reclass": recclasses,
        "mass": masses,
        "year": years,
        "reclat": reclats,
        "reclong": reclongs,
        "point coordinates": coordinates
    }

    #Create a dataframe from a dict.
    df = pd.DataFrame(meteorite_data)
    return df

def export_to_csv(df,filename):
    df.to_csv(filename,index=False)


if __name__ == "__main__":
    link = "https://data.nasa.gov/resource/y77d-th95.json"
    data = download_data_from_link(link)
    df = process_data(data)
    filename = "meteorite_data.csv"
    export_to_csv(df,filename)