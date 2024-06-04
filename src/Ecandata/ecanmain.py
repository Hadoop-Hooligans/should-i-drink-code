"""Main script for Sourcing the Ecan Data, Run as a module, will not work if run directly"""

from .ecanwrangle import clean_ecan
from .ecandata import get_ecan_data
from .downloadCsv import download_excel_workbook


def create_water_reports() -> None:
    """Query Ecan API and build up a dataframe of Wells, then create a list of well links and ids and iteratively
    Scrap the data on each well from the Ecan website. Creates a folder of csvs one for each well
    """
    all_ecan_data = get_ecan_data()
    all_ecan_data.drop_duplicates(subset="Well_No", keep="first", inplace=True)
    # Prints all the data from the API
    # wrangled_ecan_data = clean_ecan(all_ecan_data)
    all_ecan_data.to_csv("/app/src/ecan_data.csv")

    codes = all_ecan_data["Well_No"].tolist()
    print(len(codes))
    download_excel_workbook(codes)
    print("Finished Downloading")


# ids = ["BW24/0039", "K38/0088", "M35_6639", "L35_0558"]
# download_excel_workbook(ids)
# create_water_reports()
