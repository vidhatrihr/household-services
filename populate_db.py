from models import *


def populate():
  # create 1 of admin, customer, professional each
  db.session.add(Admin(
      user=User(
          email='admin1@example.com',
          password='12345',
          type='customer',
          full_name='admin 1',
          address='xyz address',
          pin_code='123456',
          city_id=1
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer1@example.com',
          password='12345',
          type='customer',
          full_name='customer 1',
          address='xyz address',
          pin_code='123456',
          city_id=1
      )
  ))
  db.session.add(Professional(
      service_category_id=1,
      user=User(
          email='professional1@example.com',
          password='12345',
          type='professional',
          full_name='professional 1',
          address='xyz address',
          pin_code='123456',
          city_id=2
      )
  ))

  # create cities
  db.session.add(City(name='hbh'))
  db.session.add(City(name='albd'))

  # create service categories and services
  db.session.add(ServiceCategory(name='Plumbing services', services=[
      Service(name='Tap repair'),
      Service(name='Heater setup'),
      Service(name='Pipe leakage')
  ]))
  db.session.add(ServiceCategory(name='Cleaning services', services=[
      Service(name='Bathroom cleaning'),
      Service(name='Kitchen cleaning'),
      Service(name='Full home cleaning')
  ]))
  db.session.commit()
