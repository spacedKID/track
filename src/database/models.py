from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class SubCategory(Base):
    __tablename__ = 'sub_categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="sub_categories")

Category.sub_categories = relationship("SubCategory", order_by=SubCategory.id, back_populates="category")

class TrackableObject(Base):
    __tablename__ = 'trackable_objects'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    sub_category_id = Column(Integer, ForeignKey('sub_categories.id'))
    data_type = Column(String)
    sub_category = relationship("SubCategory", back_populates="trackable_objects")

SubCategory.trackable_objects = relationship("TrackableObject", order_by=TrackableObject.id, back_populates="sub_category")

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    category_id = Column(Integer, ForeignKey('categories.id'))
    sub_category_id = Column(Integer, ForeignKey('sub_categories.id'))
    trackable_object_id = Column(Integer, ForeignKey('trackable_objects.id'))
    value = Column(String)  # Storing as string for simplicity; you might convert based on data_type

# Initialize the database connection (e.g., for SQLite)
engine = create_engine('sqlite:///track.db', echo=True)

# Create all tables
Base.metadata.create_all(engine)
