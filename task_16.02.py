from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine('sqlite:///homework.db', echo=True)
meta = MetaData()
groups = Table(
    'groups', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)

student = Table(
    'student', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String),
    Column('lastname', String),
    Column('group_id', Integer, ForeignKey('groups.id')),
)
meta.create_all(engine)
conn = engine.connect()
conn.execute(groups.insert(), [
    {'name': 'P-326'},
    {'name': 'P-327'},
])
conn.execute(student.insert(), [
    {'firstname': 'Vania', 'lastname': 'Kitayeu', 'group_id': 1},
    {'firstname': 'Ira', 'lastname': 'Lyutova', 'group_id': 2},
    {'firstname': 'Pasha', 'lastname': 'Dost', 'group_id': 1},
    {'firstname': 'Sasha', 'lastname': 'Frost', 'group_id': 2},
    {'firstname': 'Dasha', 'lastname': 'Karpuk', 'group_id': 1},
    {'firstname': 'Masha', 'lastname': 'Popova', 'group_id': 2},
])
