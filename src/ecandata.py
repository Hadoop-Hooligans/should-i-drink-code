"""Run this as a module"""

import pandas as pd
import requests

#################
import json

import requests

url = "https://gis.ecan.govt.nz/arcgis/rest/services/Public/Groundwater/MapServer/19/query?outFields=*&where=1%3D1&f=geojson"


def get_ecan_data():
    """Function to call the Ecan api. Returns a pandas dataframe"""
    response = requests.get(url)
    data = response.json()

    extracted_data = []
    for feature in data["features"]:
        properties = feature["properties"]
        longitude, latitude = feature["geometry"]["coordinates"]
        extracted_data.append(
            {
                "Well_No": properties["Well_No"],
                "Well_Status": properties["Well_Status"],
                "Well_Type": properties["Well_Type"],
                "Well_Owner": properties["Well_Owner"],
                "Driller": properties["Driller"],
                "Primary_Use": properties["Primary_Use"],
                "Secondary_Use": properties["Second_Use"],
                "WGS84_LONGITUDE": longitude,
                "WGS84_LATITUDE": latitude,
                "Link": properties["Link"],
                "Locality": properties["Locality"],
                "Street": properties["Street"],
            }
        )
    df = pd.DataFrame(extracted_data)
    return df
