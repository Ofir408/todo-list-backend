from flask import jsonify

from db_handler import CommandRunner
import json


class TaskGetter:

    def get_tasks(self):
        sql = "SELECT * FROM tasks"
        response = []

        cursor = CommandRunner.run(sql)
        rows = cursor.fetchall()

        for row in rows:
            data = {'id': str(row[0]), 'name': str(row[1]), 'description': str(row[2])}
            json_data = json.dumps(data)
            response.append(json.loads(json_data))
        if len(rows) == 0:
            return ""
        # response.headers.add("Access-Control-Allow-Origin", "*")

        a = jsonify(response)
        a.headers.add("Access-Control-Allow-Origin", "*")
        return a
