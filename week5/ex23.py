import os
import pathlib
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM artists")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


path = pathlib.Path()
print(repr(path))
print(os.getcwd())

print(os.path.realpath(__file__))

current_path_obj = pathlib.Path(os.getcwd())

filename = os.path.join(current_path_obj.parent, 'docs', 'chinook.db')
print(filename)

database = filename

# create a database connection
conn = create_connection(database)
with conn:
    print("1. Query task by priority:")

    print("2. Query all tasks")
    select_all_tasks(conn)




