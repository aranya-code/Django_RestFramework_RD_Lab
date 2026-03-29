# 📘 Course Management API (Django REST Framework)

A robust RESTful API built using **Django** and **Django REST Framework (DRF)** for managing course data. This project demonstrates the implementation of **class-based views using APIView**, structured serializers, and clean API response handling.

---

## 🚀 Features

- Full CRUD (Create, Read, Update, Delete) operations for courses  
- Built using Django REST Framework APIView  
- Structured JSON responses with custom messages  
- Clean separation of concerns (Model, Serializer, Views)  
- Scalable architecture with support for ViewSets and Generic Views (commented for reference)  

---

## 🏗️ Project Structure

```
courseSerializers/
│
├── courseApp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── courseSerializers/
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

## 🌐 API Endpoints

### 📌 Get All Courses / Create Course

```
GET     /course/
POST    /course/
```

- **GET** → Retrieve all courses  
- **POST** → Create a new course  

---

### 📌 Get / Update / Delete Course

```
GET     /course/<id>
PUT     /course/<id>
DELETE  /course/<id>
```

- **GET** → Retrieve a specific course  
- **PUT** → Update course details  
- **DELETE** → Delete a course  

---

## 🧠 View Logic (APIView)

- Uses `APIView` for full control over request handling  
- Custom response formatting for better API usability  
- Proper error handling using `Http404`  


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

### 5. Start Development Server

```bash
python manage.py runserver
```

---

## 🔮 Future Enhancements

- Add authentication (JWT / Token-based security)  
- Implement pagination and filtering  
- Add Swagger/OpenAPI documentation  
- Convert to ViewSets + Routers for cleaner routing  
- Add validation and rating constraints  

---

## 👨‍💻 Author

**Aranya Majumdar**

---

## ⭐ Notes

This project also includes **commented implementations** of:
- ViewSets (`ModelViewSet`)  
- Generic Views (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`)  
- Mixins-based approach  

These can be enabled for more scalable and production-ready API design.