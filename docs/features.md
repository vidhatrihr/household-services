# features

## root_bp

- ✅ GET / will redirect to login (if not logged in)
- ✅ GET / will redirect to admin/professional/customer home (if logged in)

## auth_bp

- ✅ login
- ✅ register as customer
- ✅ register as professional

## admin_bp

### `/admin/home`

- 📑 services table

  - ✅ view all services
  - ✅ add a new service
  - ✅ edit/delete an existing service
  - ✅ view (details + all requests) of a specific service

- 📑 professionals table

  - ✅ view all professionals
  - ✅ approve/block a specific professional
  - ✅ delete a specific professional
  - ✅ view (details + all requests) of a specific professional

- 📑 customers table

  - ✅ view all customers
  - ✅ view (details + all requests) of a specific customer
  - ⌛ approve/block a specific customer

- 📑 service requests table

  - ✅ view all service requests

### `/admin/search`

- search professionals

  - ✅ by full name (partially match)
  - ✅ by pin code
  - ⌛ by city (select a city)
  - ⌛ by professional id (# of professional, send to `/admin/professional-details/#`)

- search customers

  - ✅ by full name (partially match)
  - ✅ by pin code
  - ⌛ by city (select a city)
  - ⌛ by professional id (# of professional, send to `/admin/customer-details/#`)

### `/admin/summary`

- overall customer ratings

  - ✅ 5 stars? 60%, 4 stars? 20%, ...
  - ✅ pie chart

- service requests summary

  - ✅ how many requested? 150, accepted? 100, done? 300
  - ✅ bar chart

- other statistics

  - ⌛ total customers/professionals on platform
  - ⌛ total professionals per category
  - ⌛ total requests per services
  - ⌛ etc.

### details pages

- `/admin/service-details/#`

  - ✅ info about the service
  - ✅ all requests of that service
  - ⌛ show 3 tables for all requests (requested, accepted, done)
  - ⌛ links to edit/delete that service

- `/admin/professional-details/#`

  - ✅ info about the professional
  - ✅ all requests of that professional
  - ⌛ maybe show 3 tables for all requests (requested, accepted, done)

- `/admin/customer-details/#`

  - ✅ info about the customer
  - ✅ all requests of that customer
  - ⌛ maybe show 3 tables for all requests (requested, accepted, done)

### add/edit/delete a service

- ✅ on edit service page, existing values are pre-filled
- ✅ service category dropdown

### approve/block/delete a professional

- ⌛ cascade on delete?

## professional_bp

### `/professional/home`

- ⌛ not show `professional id` col in all tables

- ⌛ show `booking date` col in all tables

- ⌛ link to customer details

  - ⚠️ `/admin/customer-details/#`
  - 👍 `/professional/customer-details/#`

- 📑 accepted requests: table

  - ✅ view all accepted requests

- 📑 requests available to accept: table

  - ✅ view all requests (which not yet accepted) from professional's city and his category
  - ✅ link to accept a request

- 📑 closed requests: table

### `/professional/search`

- search accepted requests

  - ✅ by booking date
  - ✅ by pin code
  - ✅ by service

### `/professional/summary`

- overall customer ratings

  - ⌛ 5 stars? 60%, 4 stars? 20%, ...
  - ⌛ pie chart

- service requests summary

  - ⌛ how many requested? 150, accepted? 100, done? 300
  - ⌛ bar chart

## customer_bp

### `/customer/home`

- ⌛ not show `customer id` col in all tables

- ⌛ show `booking date` col in all tables

- ⌛ link to professional details

  - ⚠️ `/admin/professional-details/#`
  - 👍 `/customer/professional-details/#`

- 📑 accepted requests: table

  - ✅ view all accepted requests

- 📑 requests yet to be accepted: table

  - ✅ view all requests (which not yet accepted) sent by customer
  - ⌛ link to cancel a request

- 📑 closed requests: table

### `/customer/search`

- search services

  - ✅ by name
  - ⚠️ by pin code
  - ⌛ by category

### `/customer/summary`

- service requests summary

  - ✅ how many requested? 150, accepted? 100, done? 300
  - ✅ bar chart
