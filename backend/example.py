import aiomysql
from tornado.ioloop import IOLoop

from settings import RequestHandler


class Example(RequestHandler):
    count = 0
    def get(self):
        async def example():
            Example.count +=1
            print(Example.count)
            conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                       user='root', password='',
                                       db='mysql')
            async with conn.cursor() as cur:
                count = await cur.execute("SELECT 10")
                r = await cur.fetchall()
                print(2)
            conn.close()
            self.write({"code": 200, "msg": ""})
            self.finish()
        self._auto_finish = False
        IOLoop.current().spawn_callback(example)
