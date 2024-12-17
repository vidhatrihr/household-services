# Theory Topics

⭐ Bootstrap

- CSS framework/library
- Responsive design (e.g., table-responsive)
- Examples: form styling (form-control), buttons (btn btn-primary w-100), tables (table table-striped table-hover)

⭐ Rest API

- HTTP methods: GET, POST, PUT, DELETE
- Stateless
- JSON response
- Endpoints: e.g., /users (GET: list users, POST: create user)

⭐ CRUD (fundamental actions), HTTP Methods

- Create (POST)
- Read (GET)
- Update (PUT/PATCH)
- Delete (DELETE)

⭐ ORM

- Map DB tables to objects
- Create classes for tables
- SQLAlchemy ORM
- Easy to query, no need to write raw SQL
- Relationships: very powerful and helpful, e.g., professional.service_category.name

⭐ Git

- Version control
- Commit with a message, then push
- Tracks all code changes

⭐ Stateless

- Each request is independent
- Server and client know nothing about each other

⭐ Session

- Keeps track of logged-in users
- Uses cookies

⭐ Decorator

- Modify functions, enhance them, add functionality without modifying the code
- @ symbol
- Common: @app.route, @login_required

⭐ Matplotlib (Graphs Code)

- matplotlib.pyplot module
- Plot types: hist, pie
- Customization: labels, title

⭐ Security Mechanism

- Hashing passwords
- Using @login_required
- If current_user.type != admin: FORBIDDEN, 403

⭐ Authentication vs Authorization

- Authentication: Has a valid email/password, not an outsider (e.g., school ID card)
- Authorization: Allowed to access certain places (e.g., Can I go in the principal's room?)

⭐ Input Validation

- No @ in email? (Use type=email, not type=text)
- Use the required attribute in inputs

⭐ Werkzeug.security

- Password hashing
- generate_password_hash
- check_password_hash

---

# Questions

⭐ Truncate vs Delete (Both clear a table, erase all records)

- Truncate: Fast, no WHERE
- Delete: Slow, WHERE allowed

⭐ Validation vs Verification

- Validation: is correct data input
- Verification: is correct process/output

⭐ Types of Storage

- Volatile (temporary): RAM
- Non-volatile (persistent): HDD/SSD
- Cloud

⭐ Show MVC in Code

- Model: Data layer (DB, models)
- View: HTML templates
- Controller: Routes (Flask Routes)

⭐ Limit Username Input (<10)

- HTML: maxlength
- Python: len(input) validation

⭐ 2 Layer vs 3 Layer Protocol

- 2 Layer: Frontend + Server
- 3 Layer: Frontend + Server + Database

⭐ HTTP vs HTTPS

- HTTP: No encryption, NOT safe
- HTTPS(security): Encrypted, safe

⭐ Reset Forms

- HTML: input type=reset

⭐ Template Inheritance

- Base: \_base.html
- Child: {% extends "_base.html" %}, {% block %}

⭐ Version Control System (Git)

- Track changes
- Collaborate (others can work with you on the same code)
- Alternate name: Source control

⭐ Structured (SQL) vs Unstructured (NoSQL)

- SQL: Tables, columns, schema
- NoSQL: flexible (a row can have a special col)

⭐ Why SQL Is So Verbose?

- Expressive syntax
- Write huge queries with ease
- English-like syntax

⭐ Types of Constraints in SQL

- UNIQUE
- NULL/NOT NULL
- PRIMARY KEY
- FOREIGN KEY

⭐ Flask Advantages/Disadvantages

- Adv: Lightweight, simple, flexible
- Disadv: Manual setup and initialization of everything

⭐ Authentication vs Authorization

- Authn: Verify identity (ID card? email/password?)
- Authz: Access control (Can the customer go into the admin dashboard?)

⭐ Move Nav Bar to Footer

- HTML: Move code block

⭐ Lambda Function

- Inline function
- Syntax: lambda x: x+1
- Limited use

⭐ CSS Priority Order

- Inline > ID > Class > Tag
- !important overrides all other rules, regardless of (ID > Class > Tag)

⭐ Backref

- SQLAlchemy: Opposite side's relationships
- Example: backref="parent"

⭐ Distributed vs Client-Server

- Distributed: Multiple nodes, no central server
- Client-Server: Centralized server

⭐ LoginManager()

- Flask-Login
- Manage login sessions and logout functionality
- login_required

⭐ Hash Password

- Hashing: One-way, can't take hash and know the password
- Library: werkzeug.security

⭐ Why SQLite?

- Lightweight
- File-based
- Easy setup
- Preferred: Small apps, testing
- Alternatives (PostgreSQL): Complex queries, real-life projects, fast and optimized

⭐ Clear Button in Login

⭐ List and Tuple

- List: Mutable (can be changed)
- Tuple: Immutable (cannot be changed, can't add/remove anything once created)

⭐ Mutable and Immutable

- Mutable: Changeable (list, dict)
- Immutable: Fixed (tuple)

⭐ Primary Key vs Foreign Key

- Primary: Unique ID for each row
- Foreign: Links tables to each other

⭐ Role-Based Access Control

- Roles: Admin, customer, professional
- Forbidden, 403 if not your dashboard

⭐ Change Port Number in Code

- Flask: app.run(port=5001)

⭐ Front End vs Back End Validation

- Front: User-friendly (type=email, type=password, required)
- Back: Secure, reliable, prevents tampering (if form sent via Postman)
