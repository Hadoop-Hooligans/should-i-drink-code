import logging
import os
import requests
import time
import sys
# some IDES may not understand this import but the docker file is not complaining.
import os
import sys

# Get the full path of the current file
file_path = sys.argv[0]

# Get the base name of the file (i.e., file name with extension)
base_name = os.path.basename(file_path)

# Remove the file extension
file_name = os.path.splitext(base_name)[0]

from log_parser.log_settings import *
# call outside so function does not call gain this sets the date for the actual file.
f_date = get_frozen_datetime()

# set up the logging info and date, you only need to do this once!
send_to_log(f_date, file_name)


def download_excel_workbook(IDs):
    """Takes the url of the direct csv download link (and the ID) and downloads the csv into a folder called
    well_data"""
    baseurl = """https://www.ecan.govt.nz/data/water-quality-data/exportallsample/"""
    directory = "/app/src"
    logging.info(directory)
    print(directory)
    os.chdir(directory)  # This is important!
    if not os.path.basename(directory) == "well_data":
        message = "well data does not exist"
        logging.warning(message)
        print(message)
        os.makedirs("well_data", exist_ok=True)
        os.chdir("well_data")
        logging.info("well_data created!")

    directory = os.path.join(directory, "well_data")
    for ID in IDs:
        try:
            message = f"Downloading content for code {ID}"
            logging.info(message)
            print(message)
            n_ID = ID.replace("/", "_")
            url = baseurl + n_ID
            print(url)
            logging.info(url)
            response = requests.get(url)
            if response.status_code == 200:
                file_path = os.path.join(directory, f"{n_ID}.csv")
                print(file_path)
                logging.info(url)
                with open(file_path, "wb") as f:
                    f.write(response.content)
                    message = f"File was written at location {file_path}"
                    logging.info(message)
                    print(message)
            time.sleep(1.7)
        except Exception as e:
            message = f"There was an error downloading the file for {ID} at address: {url}, with error {e}"
            logging.error(f"There was an error downloading the file for {ID} at address: {url}, with error {e}")
            print(
                message
            )

# ids = ["BW24/0039", "K38/0088", "M35_6639", "L35_0558"]
# download_excel_workbook(ids)
