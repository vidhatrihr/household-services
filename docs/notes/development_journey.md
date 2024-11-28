## development journey

### nov 05

project planning

- identify key entities.
- list attributes for each.
- define relationships.

er diagram making

- design basic er diagram with primary keys, foreign keys and relationships.

basic flask app setup

- initialize a flask app in app.py.

sqlalchemy models

- create models.py for entities and relationships.

routes folder

- organize routes into blueprints.

blueprints

- create and configure root_bp and auth_bp blueprints.
- init.py file.

initial commit

- push code to github.

### nov 06

flask login setup

- add flask-login to manage user login.

login manager

- instantiate LoginManager and initialize in app.py.

@login_manager.user_loader

- define user loader function to retrieve user by id.

user model

- in models.py, do class User(db.Model, UserMixin) for login manager.

login form

- login form.
- basic login and logout functionality.

register

- /register
- /register/professional

dashboard templates

- create html files for each type:
  - admin: admin_home.html, admin_search.html, admin_summary.html.
  - customer: customer_home.html, customer_search.html, customer_summary.html.
  - professional: professional_home.html, professional_search.html, professional_summary.html.
- setup \_base.html as a layout template for jinja blocks (title, content, etc.)

blueprints for each type

- admin_bp: create routes for admin functionalities in admin_bp.py.
- customer_bp: create routes for customer functionalities in customer_bp.py.
- professional_bp: create routes for professional functionalities in professional_bp.py.

app.py

- register admin_bp, customer_bp, and professional_bp blueprints in app.py for app routing.

### nov 07

admin home

- display 3 tables for services, professionals, service requests.
- forms for add/edit service.

admin_bp

- routes for add/edit service
- routes for approve/block/delete professional

details

- service details (routes+templates)
- professional details (routes+templates)

### nov 08

\_tables

- macros for 4 tables
- tables can be used anywhere by calling macros as functions

utils.py file

- get_avg_ratings(professional)

details

- also have links for customer details

bootstrap

- bootstrap css in head
- bootstrap js at the end of body
- styling tables: table table-striped table-hover

admin search

- 2 forms on search page
- search professionals by name and/or pin_code
- search customers by name and/or pin_code
- admin_search.html, admin_search_results.html

admin summary

- overall customer ratings (5 stars? 60%, 4 stars? 20%, ...)
- service requests summary (requested how many? accepted? done?)
- only text data, no graphs

### nov 09

admin summary

- making plots
- using 'Agg' backend in matplotlib
- plt.pie(data, labels=labels, autopct='%1.2f%%')
- plt.bar(labels, data, color=['red', 'blue', 'green'])

admin dashboard final ✅

professional home

- show 3 tables
- accepted requests (professional has to visit customer's home and do service)
- requests available to accept (`not yet accepted` requests in professional's category, from his own city)
- closed requests (past requests that professional has done)

professional_bp

- in '/professional/home' route
- query accepted_requests, requests_available_to_accept, closed_requests

populate db

- carefully populate sample data to test professional home
- check requests in right tables, all good ✅

prof'l home done ✅

### nov 10

accept/close/book request, customer home done

`@customer_bp.route('/customer/book-service/<int:service_id>', methods=['GET', 'POST'])`

- customer_book_service.html (forms: description, booking date)

`@customer_bp.route('/customer/close-request/<int:request_id>', methods=['GET', 'POST'])`

- customer_close_request.html (forms: ratings, remarks)

customer search done✅

- customer_search.html
- customer_search_results.html

### nov 11

chores in admin_bp

- add comments
- add comment boundaries to group routes (===== summary =====)

customer summary done ✅

- chores in customer_bp
- did summary page
