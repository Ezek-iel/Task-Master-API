from flask_restful import Resource
from flask import request
from datetime import datetime
from api.models import TaskModel, Error
from api import api
from api import db


class Task(Resource):
    def get(self, task_id : str):
        taskToFetch = TaskModel.query.get(task_id)

        if taskToFetch:
            return taskToFetch.encode()
        else:
            return Error(errorType=404, details = "Task Not Found").encode()

    def put(self, task_id : str):
        
        taskToUpdate = TaskModel.query.get(task_id)
        form = request.form
        
        if taskToUpdate:
            taskToUpdate.dateTime = datetime.utcnow()
            taskToUpdate.details = form['details']
            db.session.commit()



class TaskList(Resource):
    def get(self):
        task_list = [task.encode() for task in TaskModel.query.all()]

        return {
            "tasks" : task_list
        }

    def post(self):
        form = request.form
        taskToAdd = TaskModel(details = form['details'])
        db.session.add(taskToAdd)
        db.session.commit()

api.add_resource(Task, "/task/<task_id>")
api.add_resource(TaskList, "/task")
