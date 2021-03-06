import flask
from flask import Flask, request, jsonify
import threading

from db_handler.TableCreator import TableCreator
from db_handler.TaskAdder import TaskAdder
from db_handler.TaskDeleter import TaskDeleter
from db_handler.TaskGetter import TaskGetter
from db_handler.TasksDeleter import TasksDeleter

app = Flask(__name__)

PORT = "8080"


@app.route("/api/isAlive", methods=['GET'])
def is_alive():
    return "True"


@app.route("/api/getTasks", methods=['GET'])
def get_tasks():
    task_getter = TaskGetter()
    return task_getter.get_tasks()


@app.route('/api/addTask', methods=['POST'])
def add_task():
    task = request.json["task"]
    print(task)
    task_name = task["name"]
    task_description = task["description"]
    task_adder = TaskAdder()
    return task_adder.add_task(task_name, task_description)


@app.route('/api/deleteTask', methods=['POST'])
def delete_task():
    id_to_delete = request.json['id']
    task_deleter = TaskDeleter()
    task_deleter.delete(id_to_delete)
    return "The Task Was Deleted"


@app.route('/api/deleteAll', methods=['POST'])
def delete_tasks():
    tasks_deleter = TasksDeleter()
    tasks_deleter.delete_all()
    return "All The Tasks Were Deleted"


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response


threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': PORT}).start()
# creating the db
table_creator = TableCreator()
table_creator.create_table()
