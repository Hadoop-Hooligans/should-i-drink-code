import json
import logging

import pandas as pd

import connect_to_db as connect

# Get the full path of the current file
file_name = "insert_into_acceptable_determinands"
# Remove the file extension

from log_parser.log_settings import *

# call outside so function does not call gain this sets the date for the actual file.
f_date = get_frozen_datetime()


def get_measurement_value(df, measurement):
    row = df[df['Measurement'] == measurement]
    if not row.empty:
        determinand_min_value = row.iloc[0]['Min Value']
        determinand_ideal_value = row.iloc[0]['Ideal Value']
        determinand_max_value = row.iloc[0]['Max Value']
        units = row.iloc[0]['Units']
        formula = row.iloc[0]['Formula']

        return {"determinand_name": str(measurement),
                "determinand_units": str(units),
                "determinand_formula": str(formula),
                "determinand_min_value": str(determinand_min_value),
                "determinand_ideal_value": str(determinand_ideal_value),
                "determinand_max_value": str(determinand_max_value),
                }
    else:
        return {"determinand_name": None,
                "determinand_units": None,
                "determinand_formula": None,
                "determinand_min_value": None,
                "determinand_ideal_value": None,
                "determinand_max_value": None,
                }


def insert_into_acceptable_determinands(connection, df):
    cur = connection.cursor()
    try:
        cur = connection.cursor()
        insert_into_command = """
        INSERT INTO acceptable_determinands_v2
        (
            chloride,
            hardness_total,
            calcium,
            ph,
            ph_field,
            sodium_dissolved,
            sulphate,
            water_temperature,
            oxygen_dissolved,
            magnesium,
            silica,
            nitrate_nitrogen,
            e_coli,
            total_coliforms
        )
        VALUES
        (
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb,
         %s::jsonb
        );
        """
        chloride = get_measurement_value(df, 'Chloride')
        hardness_total = get_measurement_value(df, 'Hardness, Total')
        calcium = get_measurement_value(df, 'Calcium, Dissolved')
        ph = get_measurement_value(df, 'pH')
        ph_field = get_measurement_value(df, 'pH (Field)')
        sodium_dissolved = get_measurement_value(df, 'Sodium, Dissolved')
        sulphate = get_measurement_value(df, 'Sulphate')
        water_temperature = get_measurement_value(df, 'Water Temperature (Field)')
        oxygen_dissolved = get_measurement_value(df, 'Dissolved Oxygen')
        magnesium = get_measurement_value(df, 'Magnesium, Dissolved')
        silica = get_measurement_value(df, 'Silica, Reactive')
        nitrate_nitrogen = get_measurement_value(df, 'Nitrate Nitrogen')
        e_coli = get_measurement_value(df, 'E. coli')
        total_coliforms = get_measurement_value(df, 'Total Coliforms')
        cur.execute(
            insert_into_command,
            (
                json.dumps(chloride),
                json.dumps(hardness_total),
                json.dumps(calcium),
                json.dumps(ph),
                json.dumps(ph_field),
                json.dumps(sodium_dissolved),
                json.dumps(sulphate),
                json.dumps(water_temperature),
                json.dumps(oxygen_dissolved),
                json.dumps(magnesium),
                json.dumps(silica),
                json.dumps(nitrate_nitrogen),
                json.dumps(e_coli),
                json.dumps(total_coliforms)
            ),
        )
        connection.commit()
        cur.close()
        message = "Measurement data inserted into acceptable_determinands_v2"
        logging.info(message)
        print()
    except Exception as e:
        message = f"Exception occured {e}"
        logging.error(message)
        print(message)


if __name__ == "__main__":
    acc_df = pd.read_csv('acc_deter.csv')
    connection = connect.connect_to_database()
    insert_into_acceptable_determinands(connection, acc_df)
