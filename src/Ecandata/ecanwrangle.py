"""Intended to be run as a module"""

import pandas as pd


def clean_ecan(ecan_data):
    # print(ecan_data.head(10))

    filter_by = ["Domestic Supply", "Groundwater Quality", 'Domestic and Stockwater', 'Public Water Supply',
                 'Commercial / Industrial', 'Small Community Supply', "Other - see comments"]
    filter_p_use_df = ecan_data.loc[(ecan_data['Primary_Use'].isin(filter_by)) | (
        ecan_data['Secondary_Use'].isin(filter_by))]  # We don't care about anything other than stuff people will drink
    # The api itself from what I could find did not allow for filters in the request itself.
    # print(filter_p_use_df.head(50))
    return filter_p_use_df

# import ecandata
# ecan_dataframe = ecandata.get_ecan_data()
# cleaned_ecan = clean_ecan(ecan_dataframe)
# print(cleaned_ecan)
