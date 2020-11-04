from tornado.web import RequestHandler
import json
# import db
from db import db

items = []


class TodoItems(RequestHandler):
    def get(self):
        db_instance = db()
        dbconn = db_instance.conn
        dbcursor = db_instance.cursor
        dbcursor.execute("SELECT * FROM todo")
        todo_records = dbcursor.fetchall()
        items = [{'id': row[0], 'title': row[1]}for row in todo_records]
        # todo_records format [(1, 'task-1'), (1, 'task-2'), (2, 'do HW')]
        dbconn.commit()
        self.write({'items': items})

    def post(self):
        data = json.loads(self.request.body.decode('ascii'))
        db_instance = db()
        dbconn = db_instance.conn
        dbcursor = db_instance.cursor
        dbcursor.execute(
            "INSERT INTO todo VALUES({0}, '{1}')". format(data['id'], data['title']))
        dbconn.commit()
        self.write({'item': json.loads(self.request.body.decode('ascii'))})
