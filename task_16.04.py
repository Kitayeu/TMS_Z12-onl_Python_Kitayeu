from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

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
meta.create_all(engine)
conn = engine.connect()
conn.execute(book.insert(), [
    {'title': 'The Hitchhiker’s Guide to the Galaxy', 'page_count': 771},
    {'title': 'The Lord of the Rings', 'page_count': 1707},
    {'title': 'Fahrenheit 451', 'page_count': 221},
    {'title': '1984', 'page_count': 541},
    {'title': 'The Martian Chronicles', 'page_count': 272},
])
request = student.select()
result = conn.execute(request)
for row in result:
    print(row)
conn.execute(association.insert(), [
    {'book_id': 1, 'student_id': 1},
    {'book_id': 1, 'student_id': 2},
    {'book_id': 1, 'student_id': 3},
    {'book_id': 1, 'student_id': 4},
    {'book_id': 1, 'student_id': 5},
    {'book_id': 1, 'student_id': 6},
    {'book_id': 2, 'student_id': 1},
    {'book_id': 2, 'student_id': 2},
    {'book_id': 2, 'student_id': 3},
    {'book_id': 2, 'student_id': 4},
    {'book_id': 2, 'student_id': 5},
    {'book_id': 2, 'student_id': 6},
    {'book_id': 3, 'student_id': 1},
    {'book_id': 3, 'student_id': 2},
    {'book_id': 3, 'student_id': 3},
    {'book_id': 3, 'student_id': 4},
    {'book_id': 3, 'student_id': 5},
    {'book_id': 3, 'student_id': 6},
    {'book_id': 4, 'student_id': 1},
    {'book_id': 4, 'student_id': 2},
    {'book_id': 4, 'student_id': 3},
    {'book_id': 4, 'student_id': 4},
    {'book_id': 4, 'student_id': 5},
    {'book_id': 4, 'student_id': 6},
    {'book_id': 5, 'student_id': 1},
    {'book_id': 5, 'student_id': 2},
    {'book_id': 5, 'student_id': 3},
    {'book_id': 5, 'student_id': 4},
    {'book_id': 5, 'student_id': 5},
    {'book_id': 5, 'student_id': 6},
])
