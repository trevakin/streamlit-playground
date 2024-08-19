from sqlalchemy import Column, create_engine, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Transactions(Base):
  __tablename__ = 'transactions'
  id = Column(Integer, primary_key=True)
  date = Column(Date)
  amount = Column(Float)
  description = Column(String)
  category_id = Column(Integer, ForeignKey('categories.id'))
  category = relationship('Categories')
  account = Column(String)

class Categories(Base):
  __tablename__ = 'categories'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  start_date = Column(Date)
  end_date = Column(Date)
  group_id = Column(Integer, ForeignKey('groups.id'))
  group = relationship('Groups')

class Groups(Base):
  __tablename__ = 'groups'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  start_date = Column(Date)
  end_date = Column(Date)

class Budget(Base):
  __tablename__ = 'budget'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  start_date = Column(Date)
  end_date = Column(Date)
  category_id = Column(Integer, ForeignKey('categories.id'))
  amount = Column(Float)
  
  

engine = create_engine('sqlite:///storage.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()