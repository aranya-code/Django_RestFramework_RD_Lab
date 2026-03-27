# FBV Passengers API – Django REST Framework

## Overview

FBV Passengers API is a Django REST Framework project that demonstrates how to build RESTful APIs using **Function-Based Views (FBV)** and **serializers**.

The project manages passenger data and provides API endpoints to perform CRUD operations such as creating, retrieving, updating, and deleting passenger records.

This project is part of the **Django REST Framework RD Lab**, created for learning and practicing DRF concepts.

---

## Features

- RESTful API using Django REST Framework
- Function-Based Views (FBV)
- Data serialization using DRF serializers
- JSON request and response handling
- CRUD operations through API
- Structured Django project architecture

---

## Tech Stack

Language: Python  
Framework: Django  
API Framework: Django REST Framework  
Database: SQLite  
API Testing: Browser / Postman

---

## Project Structure
```
fvbPassengers_DRF/
│
├── fvbPassengers_DRF/       # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── passengers/              # Django application
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

## Learning Objectives

This project helps in understanding:

- Django REST Framework basics
- Function-Based API views
- Serializers and data validation
- CRUD API operations
- JSON request and response handling

---

## Future Improvements

- Add authentication
- Add filtering and search
- Add pagination
- Add API documentation

---

## Author

Aranya Majumdar  
GitHub: https://github.com/aranya-code