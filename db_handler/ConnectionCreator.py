import sqlite3


class ConnectionCreator:

    @staticmethod
    def create_connection(db_file):

        connection = None
        try:
            return sqlite3.connect(db_file)
        except Exception as e:
            print(e)
        return connection
