import tornado.web

from backend.example import Example
from settings import SETTINGS

settings = SETTINGS


def make_app():
    return tornado.web.Application([
        (r"/", Example),
    ],
        **settings
    )
