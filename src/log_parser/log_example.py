import os
import sys

# Get the full path of the current file
file_path = sys.argv[0]

# Get the base name of the file (i.e., file name with extension)
base_name = os.path.basename(file_path)

# Remove the file extension
file_name = os.path.splitext(base_name)[0]

from log_settings import *
# call outside so function does not call gain this sets the date for the actual file.
f_date = get_frozen_datetime()

# set up the logging info and date, you only need to do this once!
send_to_log(f_date, file_name)

# Log a message
url = 'https://www.ecan.govt.nz/data/water-quality-data/exportallsample/'
message = f"collecting {url}"

logging.info("test")
logging.error("test")