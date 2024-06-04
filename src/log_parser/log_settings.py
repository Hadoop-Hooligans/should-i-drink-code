from .log_jsonify import *


def send_to_log(f_date, f_module="test"):
    # make sure logging directory exists.
    os.makedirs(os.path.join('..', 'logs'), exist_ok=True)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a handler
    log_dir = os.path.join('..', 'logs', f"{f_module}_{f_date}.log")
    json_handler = logging.FileHandler(log_dir)

    # Create and set the formatter
    formatter = JsonFormatter()
    json_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(json_handler)
