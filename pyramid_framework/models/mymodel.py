from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from .meta import Base
from sqlalchemy.dialects.mysql import TIME

class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    city = Column(String(100))
    street = Column(String(100))
    street_number = Column(Integer())
    open_at = Column(TIME())
    close_at = Column(TIME())


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    surname = Column(String(100))
    date_of_birth = Column(DateTime())
    id_number = Column(String(100))