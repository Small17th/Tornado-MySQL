import tornado
from urls import make_app


def run():
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
