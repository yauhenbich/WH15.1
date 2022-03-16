import sqlite3
import json


def get_data_from_db(db_name, query):
    with sqlite3.connect(db_name) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(query)
        result = dict(cursor.fetchone())

        return json.dumps(result)