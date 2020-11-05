from tornado.web import RequestHandler
import json
from services import TodoItemsService


class TodoItemsRoute(RequestHandler):
    def get(self):
        items = TodoItemsService.get(self)
        self.write({'items': items})

    def post(self):
        data = json.loads(self.request.body.decode('ascii'))
        res = TodoItemsService.post(self, data)
        self.write({'sucess': res})
