# routes

## root_bp

- GET `/`
  - if not logged in, go to `/login`
  - if logged in, check `current_user.type`
    - go to `/admin/home`
    - go to `/professional/home`
    - go to `/customer/home`

## auth_bp

- GET `/login`
  - submit email + password via form: POST `/login`
    - correct credentials: login success, go to `/`
    - incorrect credentials: login failed, stay at `/login` with jinja `error=true`
  - no account? can click on `/register` link
- GET `/register`
  - for customers
  - submit details via form: POST `/register`
    - register success, go to `/`
  - want to register as a professional? click on `/register/professional` link
- GET `/register/professional`
  - for professionals
  - submit details via form: POST `/register/professional`
    - register success, go to `/`
- GET `/logout`
  - logout, then go to `/login`

## admin_bp

- GET `/admin/home`

  - services table
    - details: `/admin/service-details/<int:service_id>`
    - add (via form)
      - GET `/admin/add-service`
      - POST `/admin/add-service`
    - edit (via form)
      - GET `/admin/edit-service/<int:service_id>`
      - POST `/admin/edit-service/<int:service_id>`
    - delete: `/admin/delete-service/<int:service_id>`
  - professionals table
    - details: `/admin/professional-details/<int:professional_id>`
    - approve: `/admin/approve-professional/<int:professional_id>`
    - block: `/admin/block-professional/<int:professional_id>`
    - delete: `/admin/delete-professional/<int:professional_id>`
  - customers table
    - details: `/admin/customer-details/<int:customer_id>`
  - service requests table
    - related professional's details: `/admin/customer-details/<int:customer_id>`
    - related customer's details: `/admin/professional-details/<int:professional_id>`

- GET `/admin/search`

  - search professionals
    - query params: `name`, `pin_code`, `city`, `professional_id`
    - apply filters: full name (partial match), ...
    - get results: list of matching professionals
  - search customers
    - query params: `name`, `pin_code`, `city`, `professional_id`
    - apply filters: full name (partial match), ...
    - get results: list of matching customers

- GET `/admin/summary`

  - overall customer ratings
    - pie chart for ratings distribution (5 stars, 4 stars, etc.)
  - service requests summary
    - bar chart for requests status: requested, accepted, done
  - other statistics
    - total customers/professionals on platform
    - total professionals per category
    - total requests per service

### routes for add/edit/delete services

- get+POST `/admin/add-service`
- get+POST `/admin/edit-service/<int:service_id>`
- GET `/admin/delete-service/<int:service_id>`

### routes for approve/block/delete professionals

- GET `/admin/approve-professional/<int:professional_id>`
- GET `/admin/block-professional/<int:professional_id>`
- GET `/admin/delete-professional/<int:professional_id>`

### routes for details of a specific service/professional/customer

- GET `/admin/service-details/<int:service_id>`
- GET `/admin/professional-details/<int:professional_id>`
- GET `/admin/customer-details/<int:customer_id>`

## professional_bp

- GET `/professional/home`
  - `accepted_requests` table
  - `requests_available_to_accept` table
  - `closed_requests` table

### routes for searching

- GET `/professional/search`
  - no query params, displays search form
- GET `/professional/search-results/<search_type>`
  - search for accepted requests
    - query params: `booking_date`, `pin_code`, `service_id`
    - apply filters
    - get results: list of matching service requests
- GET `/professional/summary`
  - summary of professional's requests

### routes for accepting requests

- GET `/professional/accept-request/<int:request_id>`
  - accepts a service request, sets status to `accepted`

## customer_bp

- GET `/customer/home`
  - `accepted_requests` table
  - `pending_requests` table
  - `past_requests` table
- GET `/customer/search`
  - no query params, displays search form
- GET `/customer/search-results/<search_type>`
  - search for services
    - query params: `name`, `pin_code`
    - apply filters: name, pin code
    - get results: list of matching services
- GET `/customer/summary`
  - displays summary of customer's requests

### routes for booking services

- GET `/customer/book-service/<int:service_id>`
  - displays form to book a service
- POST `/customer/book-service/<int:service_id>`
  - submit booking form, creates a new service request

### routes for closing requests

- GET `/customer/close-request/<int:request_id>`
  - displays form to close a request
- POST `/customer/close-request/<int:request_id>`
  - submit close request form, sets status to `done`, adds ratings and remarks
