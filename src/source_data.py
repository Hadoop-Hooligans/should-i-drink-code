from Ecandata import ecanmain

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

# from Lawadata import lawa_main

def source_data():
    """Main file for downloading the external data, Lawa data returns as a Dictionary of DF objects,
    Ecan Data is downloaded in the folder well_data"""
    print("Starting data sourcing")
    logging.info("Starting data sourcing")
    # lawa_main.get_lawa_groundwater()
    ecanmain.create_water_reports()
    print("Finished data sourcing")
    logging.info("Finished data sourcing")


source_data()
