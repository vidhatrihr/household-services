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

- 📑 service requests table

  - ✅ view all service requests

### `/admin/search`

- search professionals

  - ✅ by full name (partially match)
  - ✅ by pin code

- search customers

  - ✅ by full name (partially match)
  - ✅ by pin code

### `/admin/summary`

- overall customer ratings

  - ✅ 5 stars? 60%, 4 stars? 20%, ...
  - ✅ pie chart

- service requests summary

  - ✅ how many requested? 150, accepted? 100, done? 300
  - ✅ bar chart

### details pages

- `/admin/service-details/#`

  - ✅ info about the service
  - ✅ all requests of that service

- `/admin/professional-details/#`

  - ✅ info about the professional
  - ✅ all requests of that professional

- `/admin/customer-details/#`

  - ✅ info about the customer
  - ✅ all requests of that customer

### add/edit/delete a service

- ✅ on edit service page, existing values are pre-filled
- ✅ service category dropdown

### approve/block/delete a professional

## professional_bp

### `/professional/home`

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

  - ✅ 5 stars? 60%, 4 stars? 20%, ...
  - ✅ pie chart

- service requests summary

  - ✅ how many requested? 150, accepted? 100, done? 300
  - ✅ bar chart

## customer_bp

### `/customer/home`

- 📑 accepted requests: table

  - ✅ view all accepted requests

- 📑 requests yet to be accepted: table

  - ✅ view all requests (which not yet accepted) sent by customer

- 📑 closed requests: table

### `/customer/search`

- search services

  - ✅ by name

### `/customer/summary`

- service requests summary

  - ✅ how many requested? 150, accepted? 100, done? 300
  - ✅ bar chart
