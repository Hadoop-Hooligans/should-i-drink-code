from dotenv import dotenv_values
import psycopg2

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

def connect_to_database():
    config = dotenv_values()
    try:
        # Establish the connection
        conn = psycopg2.connect(
            dbname=config['DB_NAME'],
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
            host=config['DB_HOST'],
            port=config['DB_PORT']
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute a test query
        cur.execute("SELECT version();")

        # Fetch the result
        db_version = cur.fetchone()
        message = f"INFO: Connected to PostgreSQL database, version: {db_version}"
        logging.info(message)
        print(message)
        return conn

    except Exception as e:
        message = f"CRITICAL: unable to connect to PostgreSQL database: {e}"
        logging.critical(message)
        print(message)


def close_connection(conn):
    # Close the cursor and connection
    cur = conn.cursor()
    cur.close()
    conn.close()
