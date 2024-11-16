from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


# ======== User ========


class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String, unique=True)
  password = Column(String)
  type = Column(String)
  full_name = Column(String)
  address = Column(String)
  pin_code = Column(String)
  city_id = Column(Integer, ForeignKey('cities.id'))
  city = relationship('City', back_populates='users')
  customer = relationship('Customer', back_populates='user', uselist=False)
  professional = relationship('Professional', back_populates='user', uselist=False)
  admin = relationship('Admin', back_populates='user', uselist=False)


# ======== City ========


class City(db.Model):
  __tablename__ = 'cities'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  users = relationship('User', back_populates='city')


# ======== Admin ========


class Admin(db.Model):
  __tablename__ = 'admins'
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship('User', back_populates='admin')


# ======== Customer ========


class Customer(db.Model):
  __tablename__ = 'customers'
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship('User', back_populates='customer', cascade='all, delete')
  service_requests = relationship('ServiceRequest', back_populates='customer')


# ======== Professional ========


class Professional(db.Model):
  __tablename__ = 'professionals'
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  service_category_id = Column(Integer, ForeignKey('service_categories.id'))
  bio = Column(String)
  is_approved = Column(Boolean, default=False)
  user = relationship('User', back_populates='professional', cascade='all, delete')
  service_category = relationship('ServiceCategory', back_populates='professionals')
  service_requests = relationship('ServiceRequest', back_populates='professional')


# ======== Service Category ========


class ServiceCategory(db.Model):
  __tablename__ = 'service_categories'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  professionals = relationship('Professional', back_populates='service_category')
  services = relationship('Service', back_populates='service_category')


# ======== Service ========


class Service(db.Model):
  __tablename__ = 'services'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  price = Column(Integer)
  service_category_id = Column(Integer, ForeignKey('service_categories.id'))
  service_category = relationship('ServiceCategory', back_populates='services')
  service_requests = relationship('ServiceRequest', back_populates='service')


# ======== Service Request ========


class ServiceRequest(db.Model):
  __tablename__ = 'service_requests'
  id = Column(Integer, primary_key=True, autoincrement=True)
  customer_id = Column(Integer, ForeignKey('customers.id'))
  service_id = Column(Integer, ForeignKey('services.id'))
  description = Column(String)
  professional_id = Column(Integer, ForeignKey('professionals.id'))
  status = Column(String, default='requested')  # requested, accepted, done
  created_date = Column(DateTime, default=datetime.now)
  booking_date = Column(DateTime)
  ratings = Column(Integer, default=0)
  remarks = Column(String)
  customer = relationship('Customer', back_populates='service_requests')
  service = relationship('Service', back_populates='service_requests')
  professional = relationship('Professional', back_populates='service_requests')
