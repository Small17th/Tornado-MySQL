import aiomysql
from tornado.ioloop import IOLoop

from settings import RequestHandler


class Example(RequestHandler):
    count = 0
    def get(self):
        async def example():
            Example.count +=1
            print(Example.count)
            conn = await aiomysql.connect(host='rm-bp1d1p3ebdnt445mcqo.mysql.rds.aliyuncs.com', port=3306,
                                          user='tnzx', password='wJXB5O4JWvUP1kJQ',
                                          db='tiannengdb')
            async with conn.cursor() as cur:
                count = await cur.execute("SELECT * FROM a_tn_user_merchant limit 1")
                r = await cur.fetchall()
                print(2)
            conn.close()
            self.write({"code": 200, "msg": ""})
            self.finish()
        self._auto_finish = False
        IOLoop.current().spawn_callback(example)
