from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///homework-16.db', echo=True)
Base = declarative_base()


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.id} {self.name}"


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship("Brand", back_populates="cars")

    def __repr__(self):
        return f"{self.__class__.__name__} {self.id} {self.model} {self.release_year} {self.brand_id}"


Brand.cars = relationship("Car", order_by=Car.id, back_populates="brand")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def adding_brand(name: str) -> None:
    """Creating a new row in the 'brands' table

    :param name: brand name
    """
    entity = Brand(name=name)
    session.add(entity)
    session.commit()


def reading_brand():
    """Reading all rows from the 'brands' table"""
    result = session.query(Brand).all()
    for row in result:
        print(row)


def updating_brand(id: int, name: str) -> None:
    """Updating brand data by 'id' from the 'brands' table

    :param id: brand id
    :param name: brand name
    """
    entity = session.query(Brand).get(id)
    entity.name = name
    session.commit()


def deleting_brand(id: int) -> None:
    """Deleting a brand by 'id' from the 'brands' table

    :param id: brand id
    """
    session.query(Brand).filter(Brand.id == id).delete()
    session.commit()


def adding_car(model: str, release_year: int, brand_id: int) -> None:
    """Creating a new row in the 'cars' table

    :param model: car model
    :param release_year: release year of the car
    :param brand_id: brand id
    """
    entity = Car(model=model, release_year=release_year, brand_id=brand_id)
    session.add(entity)
    session.commit()


def reading_car():
    """Reading all rows from the 'cars' table"""
    result = session.query(Car).all()
    for row in result:
        print(row)


def updating_car(id: int, model: str, release_year: int, brand_id: int) -> None:
    """Updating car data by 'id' from the 'cars' table

    :param id: car id
    :param model: car model
    :param release_year: release year of the car
    :param brand_id: brand id
    """
    entity = session.query(Car).get(id)
    entity.model = model
    entity.release_year = release_year
    entity.brand_id = brand_id
    session.commit()


def deleting_car(id: int) -> None:
    """Deleting a car by 'id' from the 'cars' table

    :param id: car id
    """
    session.query(Car).filter(Car.id == id).delete()
    session.commit()
