from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine('sqlite:///task.db', echo=True)
meta = MetaData()
department = Table(
    'department', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)

employee = Table(
    'employee', meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String),
    Column('lastname', String),
)

association = Table(
    'association', meta,
    Column('employee_id', Integer, ForeignKey('employee.id')),
    Column('department_id', Integer, ForeignKey('department.id')),
)
meta.create_all(engine)
