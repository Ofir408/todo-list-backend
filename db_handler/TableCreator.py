import sqlite3

import Definitions


class TableCreator:

    @staticmethod
    def create_table():
        sql_create_tasks_table = """ CREATE TABLE tasks (
                                             id text NOT NULL,
                                             name text NOT NULL,
                                            description text NOT NULL
                                        ); """
        conn = None
        try:
            conn = sqlite3.connect(Definitions.DB_FILE_PATH)
        except Exception as e:
            print(e)

        if conn is not None:
            try:
                c = conn.cursor()
                c.execute(sql_create_tasks_table)
            except Exception as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")
