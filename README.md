# Flask Webapp

This repository contains a Flask web application that utilizes various libraries and tools for creating and managing a web application with a database. The application includes features such as user login, database migrations, form handling, and password hashing.

# Libraries Used

	alembic==1.11.0: Alembic is a database migration tool for SQLAlchemy. It allows for seamless management of database schema changes over time.

	flask==2.3.2: Flask is a lightweight web application framework used to create the core structure and routing of the web application.

        flask-migrate==2.4.0: Flask-Migrate is an extension for Flask that integrates Alembic for handling database migrations within the Flask application.

        flask-sqlalchemy==3.0.3: Flask-SQLAlchemy provides integration between Flask and SQLAlchemy, making it easier to work with databases in the Flask application.

flask-wtf==1.1.1: Flask-WTF is an extension for Flask that simplifies working with WTForms, a library for creating and validating forms.

wtforms==3.0.1: WTForms is a flexible forms library for Python. It is used in conjunction with Flask-WTF to create forms in the web application, such as the login form.

jinja2==3.1.2: Jinja2 is a template engine for Python. It is used by Flask to render dynamic HTML templates in the web application.

sqlalchemy==2.0.13: SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library. It provides a high-level interface for working with databases.

sqlite==3.41.2: SQLite is a lightweight, file-based database engine. It is used in this application as the backend database.

werkzeug==2.3.4: Werkzeug is a WSGI (Web Server Gateway Interface) utility library. Flask is built on top of Werkzeug and uses it to handle essential functionalities like routing, request and response handling, URL generation, and more.

email_validator==2.0.0.post2: Email Validator is a library used to validate email addresses. It provides a comprehensive validation mechanism for ensuring the correctness of email input.

bcrypt==4.0.1: Bcrypt is a password hashing library. It is used to securely hash passwords and store them in the database.

flask_bcrypt==1.0.1: Flask-Bcrypt is a Flask extension that integrates Bcrypt into Flask applications. It provides convenient methods for hashing and verifying passwords in the Flask application.

flask_login==0.6.2: Flask-Login is a Flask extension that simplifies the management of user authentication and sessions in the web application.
