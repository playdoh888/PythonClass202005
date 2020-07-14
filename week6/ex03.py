import os
from week5.ex19 import create_connection, select_all_tasks
current_directory = os.getcwd()

print(f"Current working directory name (relative name): {os.path.basename(current_directory)}")
print(f"Current script name: {os.path.realpath(__file__)}")

parent_dir = os.path.dirname(current_directory)
print(parent_dir)

database_name = os.path.join(parent_dir, "docs", "chinook.db")
print(database_name)

def select_all_employees(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")

    rows = cur.fetchall()

    for row in rows:
        print(row)

conn = create_connection(database_name)
with conn:

    print("Query all employees")
    select_all_employees(conn)


