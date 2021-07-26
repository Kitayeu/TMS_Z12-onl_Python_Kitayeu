from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float

engine = create_engine('sqlite:///homework.db', echo=True)
meta = MetaData()
student = Table(
    'student', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String),
    Column('lastname', String),
    Column('group_id', Integer, ForeignKey('groups.id')),
)

diary = Table(
    'diary', meta,
    Column('id', Integer, primary_key=True),
    Column('average_mark', Float),
    Column('student_id', Integer, ForeignKey('student.id')),
)
meta.create_all(engine)
conn = engine.connect()
request = student.select()
result = conn.execute(request)
for row in result:
    print(row)
conn.execute(diary.insert(), [
    {'average_mark': 7.5, 'student_id': 1},
    {'average_mark': 9.2, 'student_id': 2},
    {'average_mark': 6.2, 'student_id': 3},
    {'average_mark': 8.5, 'student_id': 4},
    {'average_mark': 5.5, 'student_id': 5},
    {'average_mark': 8.8, 'student_id': 6},
])
