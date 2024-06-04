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


def insert_into_well_metadata(connection, row):
    try:
        cur = connection.cursor()
        insert_into_command = """
        INSERT INTO well_metadata
        (
            well_id,
            well_status,
            well_type,
            well_owner,
            driller,
            primary_use,
            secondary_use,
            latitude,
            longitude,
            ecan_well_link,
            address_one,
            address_two
        )
        VALUES
        (
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s
        );
        """
        cur.execute(
            insert_into_command,
            (
                row["Well_No"],
                row["Well_Status"],
                row["Well_Type"],
                row["Well_Owner"],
                row["Driller"],
                row["Primary_Use"],
                row["Secondary_Use"],
                row["WGS84_LATITUDE"],
                row["WGS84_LONGITUDE"],
                row["Link"],
                row["Locality"],
                row["Street"],
            ),
        )
        connection.commit()
        message = "Well metadata Inserted"
        logging.info(message)
        print(message)
        cur.close()
    except Exception as e:
        message = f"Exception occured at {row['Well_No']} {e}"
        logging.error(message)
        print(message)
