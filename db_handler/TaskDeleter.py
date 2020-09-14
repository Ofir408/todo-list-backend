from db_handler import CommandRunner


class TaskDeleter:
    def delete(self, task_id):
        sql = "DELETE FROM tasks WHERE id='{0}'".format(task_id)
        CommandRunner.run(sql)
