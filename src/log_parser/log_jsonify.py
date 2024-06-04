import os
import json
import logging
from datetime import datetime

"""
Usage:
Use this to log messages in json format for custom systems,

Set a variable to handle the log date.

"""


def get_frozen_datetime():
    return datetime.now().strftime("%Y-%m-%d_%H-%M")


def write_file(data, f_name, args):
    """
    Writes logs to a predetermined path
    """
    with open(f_name, args) as file:
        file.write(data)
        file.write("\r")


class JsonFormatter(logging.Formatter):
    """
    Usage: Formatter to dump error message into JSON
    Params:
        file_date: a frozen date/time format that should be familiar to both windows and linux,
        use this to make sure multiple files are not made in the logs when the script is run once.
    """

    def format(self, record: logging.LogRecord):
        record_dict = {
            "level": record.levelname,
            "date": self.formatTime(record),
            "message": record.getMessage(),
            "module": record.module,
            "lineno": record.lineno,
        }
        return json.dumps(record_dict)
