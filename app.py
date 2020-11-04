from tornado.web import Application
from tornado.ioloop import IOLoop
from services import TodoItems


def make_app():
    urls = [("/", TodoItems)]
    return Application(urls)


if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
