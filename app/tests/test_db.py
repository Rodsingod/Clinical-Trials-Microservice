import os
import sqlite3
import pandas as pd

# this line will define the path to the SQLite database
dataBase_path = "./clinical_trials.db"

# this line will check if the database file exists
dataBase_exists = os.path.exists(dataBase_path)

# If db exists,connect and read the data
if dataBase_exists:
    connection = sqlite3.connect(dataBase_path)
    cursor = connection.cursor()

    # this will run the sql command to List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # If there are tables, fetch the contents of the first one
    if tables:
        table_name = tables[0][0]
        dataFrame = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 10;", connection)
        connection.close()
    else:
        dataFrame = "Database exists but has no tables."
else:
    dataFrame = "Database file does not exist."

dataFrame
