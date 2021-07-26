from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, text

engine = create_engine('sqlite:///homework.db', echo=True)
meta = MetaData()
student = Table(
    'student', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String),
    Column('lastname', String),
    Column('group_id', Integer, ForeignKey('groups.id')),
)

book = Table(
    'book', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('page_count', Integer),
)

association = Table(
    'association', meta,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('student_id', Integer, ForeignKey('student.id')),
)

groups = Table(
    'groups', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)
meta.create_all(engine)
conn = engine.connect()
conn.execute(book.insert(), [
    {'title': 'The doomed city', 'page_count': 550},
])
request = text("SELECT student.id from student WHERE group_id = "
               "(SELECT group_id FROM student WHERE firstname = 'Sasha');")
result = conn.execute(request)
for row in result:
    print(row)
conn.execute(association.insert(), [
    {'book_id': 6, 'student_id': 2},
    {'book_id': 6, 'student_id': 4},
    {'book_id': 6, 'student_id': 6},
])
