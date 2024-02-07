from api import db
from uuid import uuid4
from datetime import datetime


class TaskModel(db.Model):
    taskId = db.Column(db.String(),primary_key = True, default = str(uuid4()))
    dateTime = db.Column(db.String(), default = str(datetime.utcnow()))
    details = db.Column(db.String(), nullable = False)

    def __repr__(self) -> str:
        return f"Task <{self.details}>"
    
    def encode(self) -> dict:
        return {
            self.taskId : {
                "Date Time" : self.dateTime,
                "details" : self.details
            }
        }

class Error():
    def __init__(self, errorType : int, details : str) -> None:
        self.errorType = errorType
        self.details = details
    
    def encode(self) -> dict:
        return {self.errorType : self.details}