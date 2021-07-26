from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///homework.db', echo=True)
meta = MetaData()
groups = Table(
    'groups', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)
meta.create_all(engine)
