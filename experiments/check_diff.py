import pathlib

from ecl import Database, export_database, import_database

data_input_filepath = pathlib.Path("../datafile/Schema-3.2.xlsx")
data_output_filepath = pathlib.Path("../datafile/temp-test-schema.xlsx")
database = Database()

import_database(data_input_filepath, database)
export_database(database, data_output_filepath)
