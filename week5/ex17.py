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

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def main():
    database = r"ex16-sqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2020-06-01', '2020-06-30');
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2020-06-10', '2020-06-18')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2020-06-03', '2020-06-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)


if __name__ == '__main__':
    main()