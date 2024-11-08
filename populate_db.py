from models import *


def populate():
  # create admin
  db.session.add(Admin(
      user=User(
          email='admin1@example.com',
          password='12345',
          type='admin',
          full_name='admin 1',
          address='xyz address',
          pin_code='123456',
          city_id=1
      )
  ))

  # create customers
  db.session.add(Customer(
      user=User(
          email='customer1@example.com',
          password='12345',
          type='customer',
          full_name='gauri',
          address='xyz address',
          pin_code='123456',
          city_id=1
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer2@example.com',
          password='12345',
          type='customer',
          full_name='cmd',
          address='xyz address',
          pin_code='123455',
          city_id=1
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer3@example.com',
          password='12345',
          type='customer',
          full_name='sanika',
          address='xyz address',
          pin_code='123456',
          city_id=1
      )
  ))

  # create professionals
  db.session.add(Professional(
      service_category_id=1,
      bio='xyz bio',
      user=User(
          email='professional1@example.com',
          password='12345',
          type='professional',
          full_name='Harikesh shukla',
          address='xyz address',
          pin_code='123456',
          city_id=2
      )
  ))
  db.session.add(Professional(
      service_category_id=1,
      bio='xyz bio',
      is_approved=True,
      user=User(
          email='professional2@example.com',
          password='12345',
          type='professional',
          full_name='Vidu',
          address='xyz address',
          pin_code='123456',
          city_id=2
      )
  ))
  db.session.add(Professional(
      service_category_id=1,
      bio='xyz bio',
      is_approved=True,
      user=User(
          email='professional3@example.com',
          password='12345',
          type='professional',
          full_name='muskan',
          address='xyz address',
          pin_code='123455',
          city_id=2
      )
  ))

  # create cities
  db.session.add(City(name='hbh'))
  db.session.add(City(name='albd'))

  # create service categories and services
  db.session.add(ServiceCategory(name='Plumbing services', services=[
      Service(name='Tap repair', price=100),
      Service(name='Heater setup', price=100),
      Service(name='Pipe leakage', price=100)
  ]))
  db.session.add(ServiceCategory(name='Cleaning services', services=[
      Service(name='Bathroom cleaning', price=100),
      Service(name='Kitchen cleaning', price=100),
      Service(name='Full home cleaning', price=100)
  ]))

  # create service requests.
  db.session.add(ServiceRequest(
      customer_id=1,
      service_id=1,
      professional_id=1,
      booking_date=datetime.now(),
  ))
  db.session.add(ServiceRequest(
      customer_id=1,
      service_id=2,
      booking_date=datetime.now()
  ))
  db.session.commit()
