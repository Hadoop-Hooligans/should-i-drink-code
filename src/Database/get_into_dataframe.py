import Database.insert_into_db as insert_into_db
import pandas as pd
from Database.change_date_time_format import format_date_time


def get_main_data(well_code):
    main_df = pd.read_csv(f"well_data/{well_code}.csv", skiprows=2)
    main_df["SampleID"] = main_df["SampleID"].astype(str)
    main_df["Collection Date"] = main_df["Collection Date"].apply(
        format_date_time
    )

    samples = main_df["SampleID"].unique()

    for sample in samples:
        if sample != "nan":
            # print(sample)
            sub_df = main_df[main_df["SampleID"] == sample]
            insert_into_db.db_inserter(
                well_code=well_code,
                sample=sample,
                collection_date=sub_df["Collection Date"].iloc[0],
                sub_df=sub_df,
            )

        # insert_into_db.insert_into_recordings(well_code, sample, sub_df['Collection Date'][0])
        # sub_df.apply(insert_into_db.insert_into_sample, axis=1)
