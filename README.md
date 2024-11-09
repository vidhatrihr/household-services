│ app.py
│ LICENSE
│ README.md
│ household_services_vidhatri.pdf
│ models.py –> Classes: User, Customer, Professional, Admin, ServiceCategory, Service, ServiceRequests, City.
│ populate_db.py –> Sample data for tables.
│ test.ipynb
│ utils.py –> get_avg_ratings for admin routes.
│
├───routes
│ │ admin_bp.py –> Routes: admin_summary, admin_search, admin_home, add/edit/delete_service, manage_professionals.
│ │ auth_bp.py –> Routes: login, logout, register, register_professional.
│ │ customer_bp.py
│ │ professional_bp.py
│ │ root_bp.py –> Redirects to dashboards.
│ │ **init**.py
│
├───templates
│ \_base.html, \_tables.html
│ admin_add/edit_service.html, admin_service_details.html
│ admin_home/search/search_results.html, admin_summary.html
│ admin_customer/professional_details.html
│ customer_home/search/summary.html
│ professional_home/search/summary.html
│ login.html, register.html, register_professional.html
