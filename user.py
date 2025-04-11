import json
import os
from collections import Counter

DATA_FILE = 'tasks_users.json'

class Task:
    def __init__(self, title, description, due_date, priority, assigned_to=None, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.assigned_to = assigned_to
        self.completed = completed

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Task(**data)

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} - {self.description} - Due: {self.due_date} - Priority: {self.priority} - Assigned To: {self.assigned_to} - Status: {status}"

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "username": self.username,
            "tasks": [t.to_dict() for t in self.tasks]
        }

    @staticmethod
    def from_dict(data):
        user = User(data["username"])
        user.tasks = [Task.from_dict(td) for td in data["tasks"]]
        return user
