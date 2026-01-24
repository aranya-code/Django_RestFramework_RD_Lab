# Employees DRF

A Django backend project demonstrating a clean and scalable project structure for managing employee-related data.  
This project is suitable for learning Django fundamentals and can be easily extended using Django Rest Framework (DRF).

---

## 🚀 Project Overview

**Employees DRF** is a Django project built with clarity and best practices in mind.  
It separates application logic from project configuration, uses environment variables for sensitive data, and follows Django’s recommended layout.

This project is ideal for:
- Django beginners
- Backend-focused learning
- Serving as a base for REST API development

---

## 📂 Project Structure

EMPLOYEES_DRF/
├── firstApp/ # Main Django application
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── firstproject/ # Django project configuration
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── .env # Environment variables (ignored by Git)
├── db.sqlite3 # Development database
├── manage.py
├── newEmployeeDB.sql # SQL dump / reference file
└── README.md



---

## 🛠️ Tech Stack

- **Language:** Python  
- **Framework:** Django  
- **Database:** SQLite (development)  
- **Environment Management:** `.env` file  

---

## 📋 Prerequisites

Make sure you have the following installed:

- Python 3.9+
- pip



