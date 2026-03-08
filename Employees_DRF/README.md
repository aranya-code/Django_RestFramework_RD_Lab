# Employees API – Django REST Framework

## Overview

Employees API is a simple RESTful API built using **Django REST Framework (DRF)**.  
The project demonstrates how to create and manage employee data through API endpoints using Django models, serializers, and views.

Django REST Framework is a powerful toolkit for building Web APIs in Django, providing features such as serialization, authentication, and browsable APIs.

This project is part of the **Django REST Framework RD Lab**, created for learning and practicing DRF concepts.

---

## Features

- Create Employee records
- Retrieve employee data
- Update employee information
- Delete employee records
- RESTful API endpoints
- JSON response handling
- Django REST Framework serializers

---

## Tech Stack

Language: Python  
Framework: Django  
API Framework: Django REST Framework  
Database: SQLite  
Tools: Postman / Browser API testing

---

## Project Structure
```
Employees_DRF/
│
├── Employees_DRF/          # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── employees/              # Django application
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── db.sqlite3
├── manage.py
└── README.md
```
---

## API Endpoints Example

| Method | Endpoint | Description |
|------|------|------|
| GET | /emp/ | Retrieve all employees |


---

## Learning Objectives

This project helps in understanding:

- Django REST Framework basics
- Creating serializers
- Building RESTful APIs
- Handling HTTP methods (GET, POST, PUT, DELETE)
- API testing using browser or Postman

---

## Future Improvements

- Add authentication
- Add pagination
- Add filtering and search
- Improve API documentation

---

## Repository

https://github.com/aranya-code/Django_RestFramework_RD_Lab


## Author

Aranya Majumdar  
GitHub: https://github.com/aranya-code
