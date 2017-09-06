# Monk-sqlalchemy

A python async Mysql orm base on aiomysql. Now only support simple *select*,
*delete* ,*insert*.

## GetStart

### define a model

```python

from monk_sqlalchemy import orm

class User(orm.Model):
    user_id = orm.Integer(primary_key=True)
    name = orm.String(legth=255,default=None)

```

### connection

```python

  await conn.connection(loop=loop, **sql_config)

```

### insert 

```python

c1 = User(name='su')
await c1.save()

```

### select

#### get all

```python
User.all()
```

#### get by condition

```python
User.find_by(id=1)
```