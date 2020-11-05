from tornado.web import RequestHandler
import json
# import db
from db import db


class TodoItems(RequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_instance = db()
        self.dbconn = self.db_instance.conn
        self.dbcursor = self.db_instance.cursor

    def get(self):
        self.dbcursor.execute("SELECT * FROM todo")
        todo_records = self.dbcursor.fetchall()
        items = [{'id': row[0], 'title': row[1]}for row in todo_records]
        # todo_records format [(1, 'task-1'), (1, 'task-2'), (2, 'do HW')]
        self.dbconn.commit()
        self.write({'items': items})

    def post(self):
        data = json.loads(self.request.body.decode('ascii'))
        self.dbcursor.execute(
            "INSERT INTO todo VALUES({0}, '{1}')". format(data['id'], data['title']))
        self.dbconn.commit()
        self.write({'item': json.loads(self.request.body.decode('ascii'))})
