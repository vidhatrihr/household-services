from models import *


def populate():

  # create cities
  db.session.add(City(name='Mumbai'))
  db.session.add(City(name='Delhi'))
  db.session.add(City(name='Bengaluru'))
#   db.session.add(City(name='Pune'))

  # create admin
  db.session.add(Admin(
      user=User(
          email='admin1@example.com',
          password='12345',
          type='admin',
          full_name='admin',
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
          full_name='Charul Sharma',
          address='xyz address',
          pin_code='123455',
          city_id=1
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer2@example.com',
          password='12345',
          type='customer',
          full_name='Chandrashekar',
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
          full_name='Charan Kumar',
          address='xyz address',
          pin_code='123456',
          city_id=2
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer4@example.com',
          password='12345',
          type='customer',
          full_name='Chirag Chopra',
          address='xyz address',
          pin_code='123456',
          city_id=2
      )
  ))

  # create professionals
  db.session.add(Professional(
      service_category_id=1,
      is_approved=True,
      bio='xyz bio',
      user=User(
          email='professional1@example.com',
          password='12345',
          type='professional',
          full_name='Pranav Patel',
          address='xyz address',
          pin_code='123456',
          city_id=1
      )
  ))
  db.session.add(Professional(
      service_category_id=2,
      bio='xyz bio',
      is_approved=True,
      user=User(
          email='professional2@example.com',
          password='12345',
          type='professional',
          full_name='Priya Verma',
          address='xyz address',
          pin_code='123456',
          city_id=1
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
          full_name='Priti Phadke',
          address='xyz address',
          pin_code='123455',
          city_id=2
      )
  ))
  db.session.add(Professional(
      service_category_id=2,
      bio='xyz bio',
      is_approved=True,
      user=User(
          email='professional4@example.com',
          password='12345',
          type='professional',
          full_name='Pavan Sharma',
          address='xyz address',
          pin_code='123455',
          city_id=2
      )
  ))
  db.session.add(Professional(
      service_category_id=3,
      bio='xyz bio',
      is_approved=False,
      user=User(
          email='professional5@example.com',
          password='12345',
          type='professional',
          full_name='Piyush Pathak',
          address='xyz address',
          pin_code='123457',
          city_id=3
      )
  ))

  # create service categories and services
  db.session.add(ServiceCategory(name='Plumbing services', services=[
      Service(name='Tap repair', price=990),
      Service(name='Heater setup', price=850),
      Service(name='Pipe leakage', price=1099)
  ]))
  db.session.add(ServiceCategory(name='Home Improvement', services=[
      Service(name='Kitchen installation', price=1990),
      Service(name='Flooring and tiling', price=1050),
      Service(name='Furniture assembly and repair', price=1090)
  ]))
  db.session.add(ServiceCategory(name='Cleaning services', services=[
      Service(name='Bathroom cleaning', price=999),
      Service(name='Kitchen cleaning', price=999),
      Service(name='Full home cleaning', price=1990)
  ]))

  # create service requests.
  # Mumbai (accepted)
  db.session.add(ServiceRequest(
      customer_id=1,
      professional_id=1,
      service_id=1,
      booking_date=datetime(2025, 1, 10),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=2,
      professional_id=1,
      service_id=2,
      booking_date=datetime(2025, 1, 15),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=2,
      professional_id=2,
      service_id=4,
      booking_date=datetime(2025, 1, 20),
      status='accepted'
  ))

  # Mumbai (requested)
  db.session.add(ServiceRequest(
      customer_id=1,
      service_id=3,
      professional_id=1,
      booking_date=datetime(2024, 12, 1),
      status='requested'
  ))
  db.session.add(ServiceRequest(
      customer_id=2,
      service_id=5,
      professional_id=2,
      booking_date=datetime(2024, 12, 10),
      status='requested'
  ))

  # Mumbai (done)
  db.session.add(ServiceRequest(
      customer_id=2,
      service_id=1,
      professional_id=1,
      booking_date=datetime(2024, 12, 1),
      status='done',
      ratings=5
  ))
  db.session.add(ServiceRequest(
      customer_id=1,
      service_id=6,
      professional_id=2,
      booking_date=datetime(2024, 12, 10),
      status='done',
      ratings=4
  ))

  # Delhi (accepted)
  db.session.add(ServiceRequest(
      customer_id=3,
      professional_id=1,
      service_id=1,
      booking_date=datetime(2025, 1, 10),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=3,
      professional_id=1,
      service_id=2,
      booking_date=datetime(2025, 1, 15),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=4,
      professional_id=2,
      service_id=4,
      booking_date=datetime(2025, 1, 20),
      status='accepted'
  ))

  # Delhi (requested)
  db.session.add(ServiceRequest(
      customer_id=3,
      service_id=3,
      professional_id=3,
      booking_date=datetime(2024, 12, 1),
      status='requested'
  ))
  db.session.add(ServiceRequest(
      customer_id=4,
      service_id=5,
      professional_id=4,
      booking_date=datetime(2024, 12, 10),
      status='requested'
  ))
  # Delhi (done)
  db.session.add(ServiceRequest(
      customer_id=3,
      service_id=6,
      professional_id=4,
      booking_date=datetime(2024, 12, 10),
      status='done',
      ratings=3
  ))
  db.session.add(ServiceRequest(
      customer_id=4,
      service_id=3,
      professional_id=3,
      booking_date=datetime(2024, 12, 10),
      status='done',
      ratings=2
  ))
  db.session.commit()
