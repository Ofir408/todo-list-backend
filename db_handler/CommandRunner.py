import sqlite3

import Definitions


def run(sql, args=None):
    global response
    conn = None
    try:
        conn = sqlite3.connect(Definitions.DB_FILE_PATH)
    except Exception as e:
        print("exception was caught")
        print(e)

    if conn is not None:
        try:
            c = conn.cursor()
            if args is not None:
                response = c.execute(sql, args)
            response = c.execute(sql)
            conn.commit()
            return response
        except Exception as e:
            print("exception was caught")
            print(e)
    else:
        print("Error! cannot create the database connection.")
