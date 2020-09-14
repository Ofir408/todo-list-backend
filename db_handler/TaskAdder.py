from db_handler import CommandRunner
from db_handler.TaskGetter import TaskGetter
import uuid


class TaskAdder:

    def add_task(self, name, description):
        unique_id = str(uuid.uuid4())
        sql = "INSERT INTO tasks (id,name,description) VALUES ('{0}', '{1}', '{2}')".format(unique_id, name, description)
        CommandRunner.run(sql)
        task_getter = TaskGetter()
        return task_getter.get_tasks()
