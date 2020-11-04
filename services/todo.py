from tornado.web import RequestHandler
import json
# import db
from db import db

items = []


class TodoItems(RequestHandler):
    def get(self):
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
