from tornado.web import Application
from tornado.ioloop import IOLoop
from services import TodoItems
from db import Db


def make_app():
    urls = [("/", TodoItems, dict(db_instance=Db))]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
