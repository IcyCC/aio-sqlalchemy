from monk_sqlalchemy import orm
from monk_sqlalchemy import conn
import asyncio


class User(orm.Model):
    user_id = orm.Integer(primary_key=True)
    name = orm.String(legth=255,default=None)

async def init_connection():
    await conn.connection(loop=loop, **sql_config)

async def add_one(user):
    await user.save()

async def get_all():
    all = await User.all()
    return all

async def get_by_id():
    a = await User.find_by(user_id=1)
    return a[0]

async def update(id,name):
    a = await User.find_by(user_id=id)
    await a[0].update(name=name)

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


c1 = User(name='su')
c2 = User(name="peter")

loop.run_until_complete(init_connection())


# a1 = loop.run_until_complete(asyncio.wait([add_one(c1),add_one(c2)]))
loop.run_until_complete(update(3,'pig'))

# a2 = loop.run_until_complete(get_all())
# print(len(a))

# a3 = loop.run_until_complete(get_by_id())
loop.close()


