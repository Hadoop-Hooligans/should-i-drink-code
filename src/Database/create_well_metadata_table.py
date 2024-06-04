# logging
#import logging

import os
import sys

# Get the full path of the current file
file_path = sys.argv[0]

# Get the base name of the file (i.e., file name with extension)
base_name = os.path.basename(file_path)

# Remove the file extension
file_name = os.path.splitext(base_name)[0]

from ..log_parser.log_settings import *
# call outside so function does not call gain this sets the date for the actual file.
f_date = get_frozen_datetime()

# set up the logging info and date, you only need to do this once!
send_to_log(f_date, file_name)

def create_well_metadata_table(connection):
    try:
        cur = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS well_metadata (
        well_id VARCHAR(255),
        well_status VARCHAR(255),
        well_type VARCHAR(255),
        well_owner VARCHAR(255),
        driller VARCHAR(255),
        primary_use VARCHAR(255),
        secondary_use VARCHAR(255),
        latitude DOUBLE PRECISION NOT NULL,
        longitude DOUBLE PRECISION NOT NULL,
        ecan_well_link VARCHAR(255),
        address_one VARCHAR(255),
        address_two VARCHAR(255),
        PRIMARY KEY (well_id)
        )
        """ 

        cur.execute(create_table_query)
        connection.commit()
        cur.close()
        message = "Table Well Metadata created successfully"
        logging.info("Table Well Metadata created successfully")
        print(message)
    except Exception as e:
        message = f"unable to create table {e}"
        logging.error(message)
        print(message)
