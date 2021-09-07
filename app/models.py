from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()


class Continent(Base):
    __tablename__ = "continent"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    population = Column(Integer)
    area = Column(Integer)

    country = relationship("Country", backref="continents")


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    population = Column(Integer)
    area = Column(Integer)
    no_hospitals = Column(Integer)
    no_national_park = Column(Integer)

    continent_id = Column(Integer, ForeignKey("continent.id"))

    city = relationship("City", backref="country")


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    population = Column(Integer)
    area = Column(Integer)
    country_id = Column(Integer, ForeignKey("country.id"))
