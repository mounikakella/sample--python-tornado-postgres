from tornado.web import Application
from tornado.ioloop import IOLoop
from routes import TodoItemsRoute


def make_app():
    urls = [("/", TodoItemsRoute)]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
