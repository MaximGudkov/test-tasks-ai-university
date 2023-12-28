from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///employees.db', echo=True)
metadata = MetaData()
Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.salary}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
