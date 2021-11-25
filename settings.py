import tornado.web

# 日志配置
from tornado.options import define



SETTINGS = dict(
)

# 自定义启动端口
define("port", default=9999, help='run on the given port', type=int)


class RequestHandler(tornado.web.RequestHandler):


    pass

