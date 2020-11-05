from .todo import TodoItemsService
from .db import Dbservice
from .todo import TodoItemsService


class Services:
    def __init__(self):
        self.services = {
            'todo': TodoItemsService(),
            'db': Dbservice()
        }
