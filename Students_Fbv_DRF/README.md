# 📘 Student Management API (Django REST Framework)

A simple and scalable RESTful API built using **Django** and **Django REST Framework (DRF)** to manage student records. This project demonstrates CRUD operations using function-based views and serializers.

---

## 🚀 Features

- Create, Read, Update, Delete (CRUD) operations for students  
- RESTful API design using Django REST Framework  
- JSON-based request/response handling  
- Lightweight and easy to extend  

---

## 🏗️ Project Structure

```
fvbSerializers/
│
├── fvbApp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── fvbSerializers/
│   ├── urls.py
│
└── manage.py
```

---

## 📦 Tech Stack

- Python  
- Django  
- Django REST Framework  

---

## 🧩 Model

The `Student` model defines the structure of student data:

- `id` – Primary key  
- `name` – Student name  
- `score` – Marks/score  

```

---

## 🌐 API Endpoints

### 1. Get All Students / Create Student

```
GET     /students/
POST    /students/
```

- **GET** → Retrieve all students  
- **POST** → Create a new student  

---

### 2. Get / Update / Delete Single Student

```
GET     /students/<id>
PUT     /students/<id>
DELETE  /students/<id>
```

- **GET** → Retrieve a specific student  
- **PUT** → Update student details  
- **DELETE** → Remove a student  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install django djangorestframework
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Server

```bash
python manage.py runserver
```

---

## 📌 Future Improvements

- Add authentication (JWT / Token-based)  
- Pagination & filtering  
- Class-based views or ViewSets  
- API documentation (Swagger / Redoc)  
- Input validation enhancements  

---

## 👨‍💻 Author

**Aranya Majumdar**