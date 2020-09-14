from db_handler import CommandRunner


class TasksDeleter:
    def delete_all(self):
        sql = "DELETE FROM tasks"
        CommandRunner.run(sql)
