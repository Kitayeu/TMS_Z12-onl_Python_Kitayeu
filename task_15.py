from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, between

engine = create_engine('sqlite:///home_task.db', echo=True)
meta = MetaData()
user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String),
    Column('lastname', String),
    Column('age', Integer),
)
meta.create_all(engine)
conn = engine.connect()
conn.execute(user.insert(), [
    {'firstname': 'Vania', 'lastname': 'Kitayeu', 'age': 28},
    {'firstname': 'Ira', 'lastname': 'Lyutova', 'age': 31},
    {'firstname': 'Pasha', 'lastname': 'Dost', 'age': 16},
    {'firstname': 'Sasha', 'lastname': 'Frost', 'age': 18},
    {'firstname': 'Dasha', 'lastname': 'Karpuk', 'age': 24},
])
request = user.select().where(user.c.firstname == 'Vania')
result = conn.execute(request)
for row in result:
    print(row)
request_one = user.select().where(user.c.age < 25)
result_one = conn.execute(request_one)
for row in result_one:
    print(row)
request_two = user.select().where(between(user.c.age, 15, 18))
result_two = conn.execute(request_two)
for row in result_two:
    print(row)
