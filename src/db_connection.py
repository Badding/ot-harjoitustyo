import sqlite3
import os

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, 'db.sqlite'))
connection.row_factory = sqlite3.Row


def get_connection():
    return connection
