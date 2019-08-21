import db as db
from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def index() -> str:
    conn = db.get_connection()

    # user: {
    #     "user_id": "1333463",
    #     "user_name": "Eric Wu",
    #     "password": "123456"
    # }

    db.create_user(db.get_connection(), '1333463', 'Eric Wu', 'helloworld01')

    user_name = db.select_user_by_user_id(conn, '1333463')

    return json.dumps({'a user inserted': user_name })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')