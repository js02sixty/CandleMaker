from datetime import datetime
from sqlalchemy import Column, Table, Integer, String, \
    Text, DateTime, Numeric
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class UserGroup(Base):
    __tablename__ = 'user_groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    users = relationship('User', backref='group')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(30))
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(30))
    group_id = Column(Integer, ForeignKey('user_groups.id'))
    created = Column(DateTime, default=datetime.utcnow)
    edited = Column(DateTime, onupdate=datetime.utcnow())


product_note = Table('product_notes', Base.metadata,
                     Column('product_id', Integer, ForeignKey('products.id')),
                     Column('notes_id', Integer, ForeignKey('notes.id'))
                     )


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    description = Column(Text)
    weight = Column(Numeric(precision=8, scale=4))
    price = Column(Numeric(precision=5, scale=2))
    pic_url = Column(String(30))
    category_id = Column(Integer)
    notes = relationship('Note', secondary=product_note,
                         backref='products', single_parent=True, cascade="all, delete-orphan")
    created = Column(DateTime, default=datetime.utcnow)
    edited = Column(DateTime, onupdate=datetime.utcnow())


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    note = Column(Text, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    edited = Column(DateTime, onupdate=datetime.utcnow())


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True)
    category = Column(String(30))


class ProductType(Base):
    __tablename__ = 'product_types'
    id = Column(Integer, primary_key=True)
    type = Column(String(30))