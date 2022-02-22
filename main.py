import sqlite3
from flask import Flask
import json

app = Flask(__name__)

@app.get("/<itemid>")
def get_item(itemid):
    with sqlite3.connect("test.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(
            f'''
            SELECT *
            FROM animals a
            JOIN animal_type at2
            WHERE a."index" = {itemid}
            '''
        ).fetchone()

    result = dict(result)

    return app.response_class(
        json.dumps(result),
        status=200,
        mimetype="application/json"
    )

if __name__ == '__main__':
    app.run(host="localhost", port=8080)


