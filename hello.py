from monk_sqlalchemy import orm
from monk_sqlalchemy import conn
import asyncio


class User(orm.Model):
    user_id = orm.Integer(primary_key=True)
    name = orm.String(legth=255,default=None)

async def add_one(user):
    await conn.connection(loop=loop, **sql_config)
    a = await User.all()
    return a
sql_config = dict(host='127.0.0.1',
                  port=3306,
                  user='root',
                  password='root',
                  db='test',
                  charset='utf8',
                  autocommit=True,
                  maxsize=10,
                  minsize=1,
                 )

loop = asyncio.get_event_loop()


c = User(user_id=1, name='su')

a=loop.run_until_complete(add_one(c))
print(a[0].name)





