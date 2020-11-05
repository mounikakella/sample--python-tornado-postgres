from tornado.web import RequestHandler
from .db import Dbservice


class TodoItemsService():
    def __init__(self):
        self.db_instance = Dbservice()
        self.dbconn = self.db_instance.conn
        self.dbcursor = self.db_instance.cursor

    def get(self):
        dbcursor = self.dbcursor
        dbconn = self.dbconn
        dbcursor.execute("SELECT * FROM todo")
        todo_records = dbcursor.fetchall()
        items = [{'id': row[0], 'title': row[1]}for row in todo_records]
        # todo_records format [(1, 'task-1'), (1, 'task-2'), (2, 'do HW')]
        dbconn.commit()
        return items

    def post(self, data):
        self.dbcursor.execute(
            "INSERT INTO todo VALUES({0}, '{1}')". format(data['id'], data['title']))
        self.dbconn.commit()
        return True
