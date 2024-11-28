from werkzeug.security import generate_password_hash
from models import *


def populate():
  # create cities
  db.session.add(City(name='Mumbai'))
  db.session.add(City(name='Delhi'))
  db.session.add(City(name='Bengaluru'))

  # create admin
  db.session.add(Admin(
      user=User(
          email='admin1@example.com',
          password=generate_password_hash('GgJI0lQ4X'),
          type='admin',
          full_name='admin',
          address='Xyz Address',
          pin_code='123456',
          city_id=1
      )
  ))

  # create customers
  db.session.add(Customer(
      user=User(
          email='customer1@example.com',
          password=generate_password_hash('12345'),
          type='customer',
          full_name='Charul Sharma',
          address='Xyz Address',
          pin_code='123456',
          city_id=1
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer2@example.com',
          password=generate_password_hash('12345'),
          type='customer',
          full_name='Chandrashekar',
          address='Xyz Address',
          pin_code='123455',
          city_id=1
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer3@example.com',
          password=generate_password_hash('12345'),
          type='customer',
          full_name='Charan Kumar',
          address='Xyz Address',
          pin_code='123456',
          city_id=2
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer4@example.com',
          password=generate_password_hash('12345'),
          type='customer',
          full_name='Chirag Chopra',
          address='Xyz Address',
          pin_code='123455',
          city_id=2
      )
  ))

  # create professionals
  db.session.add(Professional(
      service_category_id=1,
      is_approved=True,
      bio='Xyz Bio',
      user=User(
          email='professional1@example.com',
          password=generate_password_hash('12345'),
          type='professional',
          full_name='Pranav Patel',
          address='Xyz Address',
          pin_code='123456',
          city_id=1
      )
  ))
  db.session.add(Professional(
      service_category_id=2,
      bio='Xyz Bio',
      is_approved=True,
      user=User(
          email='professional2@example.com',
          password=generate_password_hash('12345'),
          type='professional',
          full_name='Priya Verma',
          address='Xyz Address',
          pin_code='123455',
          city_id=1
      )
  ))
  db.session.add(Professional(
      service_category_id=1,
      bio='Xyz Bio',
      is_approved=True,
      user=User(
          email='professional3@example.com',
          password=generate_password_hash('12345'),
          type='professional',
          full_name='Priti Pandey',
          address='Xyz Address',
          pin_code='123454',
          city_id=2
      )
  ))
  db.session.add(Professional(
      service_category_id=2,
      bio='Xyz Bio',
      is_approved=True,
      user=User(
          email='professional4@example.com',
          password=generate_password_hash('12345'),
          type='professional',
          full_name='Pavan Sharma',
          address='Xyz Address',
          pin_code='123453',
          city_id=2
      )
  ))
  db.session.add(Professional(
      service_category_id=3,
      bio='Xyz Bio',
      is_approved=False,
      user=User(
          email='professional5@example.com',
          password=generate_password_hash('12345'),
          type='professional',
          full_name='Piyush Pathak',
          address='Xyz Address',
          pin_code='123452',
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
      booking_date=datetime(2025, 1, 15),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=1,
      professional_id=1,
      service_id=2,
      booking_date=datetime(2025, 1, 16),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=1,
      professional_id=2,
      service_id=4,
      booking_date=datetime(2025, 1, 17),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=2,
      professional_id=1,
      service_id=3,
      booking_date=datetime(2025, 1, 15),
      status='accepted'
  ))

  # Mumbai (requested)
  db.session.add(ServiceRequest(
      customer_id=1,
      service_id=2,
      booking_date=datetime(2024, 12, 1),
      status='requested'
  ))
  db.session.add(ServiceRequest(
      customer_id=1,
      service_id=3,
      booking_date=datetime(2024, 12, 1),
      status='requested'
  ))
  db.session.add(ServiceRequest(
      customer_id=1,
      service_id=5,
      booking_date=datetime(2024, 12, 1),
      status='requested'
  ))
  db.session.add(ServiceRequest(
      customer_id=2,
      service_id=5,
      booking_date=datetime(2024, 12, 2),
      status='requested'
  ))

  # Mumbai (done)
  db.session.add(ServiceRequest(
      customer_id=1,
      professional_id=1,
      service_id=1,
      booking_date=datetime(2024, 11, 1),
      status='done',
      ratings=5
  ))
  db.session.add(ServiceRequest(
      customer_id=1,
      professional_id=1,
      service_id=2,
      booking_date=datetime(2024, 11, 1),
      status='done',
      ratings=5
  ))
  db.session.add(ServiceRequest(
      customer_id=2,
      professional_id=2,
      service_id=6,
      booking_date=datetime(2024, 11, 2),
      status='done',
      ratings=4
  ))

  # Delhi (accepted)
  db.session.add(ServiceRequest(
      customer_id=3,
      professional_id=3,
      service_id=1,
      booking_date=datetime(2025, 1, 10),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=3,
      professional_id=3,
      service_id=2,
      booking_date=datetime(2025, 1, 15),
      status='accepted'
  ))
  db.session.add(ServiceRequest(
      customer_id=4,
      professional_id=4,
      service_id=4,
      booking_date=datetime(2025, 1, 20),
      status='accepted'
  ))

  # Delhi (requested)
  db.session.add(ServiceRequest(
      customer_id=3,
      service_id=3,
      booking_date=datetime(2024, 12, 1),
      status='requested'
  ))
  db.session.add(ServiceRequest(
      customer_id=4,
      service_id=5,
      booking_date=datetime(2024, 12, 10),
      status='requested'
  ))

  # Delhi (done)
  db.session.add(ServiceRequest(
      customer_id=3,
      professional_id=4,
      service_id=6,
      booking_date=datetime(2024, 12, 10),
      status='done',
      ratings=3
  ))
  db.session.add(ServiceRequest(
      customer_id=4,
      professional_id=3,
      service_id=3,
      booking_date=datetime(2024, 12, 10),
      status='done',
      ratings=2
  ))

  # to have a ratings=1
  db.session.add(ServiceRequest(
      customer_id=4,
      professional_id=3,
      service_id=3,
      booking_date=datetime(2024, 12, 10),
      status='done',
      ratings=1
  ))
  db.session.commit()
