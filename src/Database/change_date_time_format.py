from datetime import datetime


def format_date_time(date_str):
    date_obj = datetime.strptime(date_str, '%d-%b %Y %H:%M%p')
    formatted_date = date_obj.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date
