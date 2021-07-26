from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///homework-15.db', echo=True)
Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    amount = Column(Integer)
    note = Column(String)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.id} {self.name} {self.price} {self.amount} {self.note}"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def adding(name: str, price: float, amount: int, note: str) -> None:
    """Creating a new row in the 'products' table

    :param name: product name
    :param price: product price
    :param amount: product amount
    :param note: comment for the product
    """
    entity = Products(name=name, price=price, amount=amount, note=note)
    session.add(entity)
    session.commit()


def reading():
    """Reading all rows from the 'products' table"""
    result = session.query(Products).all()
    for row in result:
        print(row)


def updating(id: int, name: str, price: float, amount: int, note: str) -> None:
    """Updating product data by 'id' from the 'products' table

    :param id: product id
    :param name: product name
    :param price: product price
    :param amount: product amount
    :param note: comment for the product
    """
    entity = session.query(Products).get(id)
    entity.name = name
    entity.price = price
    entity.amount = amount
    entity.note = note
    session.commit()


def deleting(id: int) -> None:
    """Deleting a product by 'id' from the 'products' table

    :param id: product id
    """
    session.query(Products).filter(Products.id == id).delete()
    session.commit()
