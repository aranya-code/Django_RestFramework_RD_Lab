# CBV Serializers API – Django REST Framework

## Overview

CBV Serializers API is a Django REST Framework project that demonstrates how to build RESTful APIs using **Class-Based Views (CBVs)** and **serializers**. The project shows how to convert Django model data into JSON responses and handle API requests such as creating, retrieving, updating, and deleting records.

This project is part of the **Django REST Framework RD Lab**, created for learning and practicing DRF concepts.

---

## Features

- RESTful API built using Django REST Framework
- Class-Based Views for API endpoints
- Data serialization using DRF serializers
- JSON response handling
- CRUD operations through API
- Organized Django project structure

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
cbvserializers_DRF/
│
├── cbvserializers_DRF/      # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/                     # Django application
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
- Serializers and data validation
- Class-Based API views
- CRUD operations in APIs
- JSON response handling

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