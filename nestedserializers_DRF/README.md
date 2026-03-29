# 📘 Nested Serializer API (Django REST Framework)

A RESTful API built using **Django** and **Django REST Framework (DRF)** demonstrating **nested serializers** with a one-to-many relationship between Authors and Books.

This project showcases how to structure APIs using **ModelViewSet**, **routers**, and **nested data representation**.

---

## 🚀 Features

- Full CRUD operations for Authors and Books  
- Nested serializer implementation (Author → Books)  
- Clean and scalable API using DRF ViewSets  
- Automatic routing using DefaultRouter  
- One-to-many relationship handling (ForeignKey)  
- JSON-based API responses  

---

## 🏗️ Project Structure

```
nestedserializers/
│
├── NestedApp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── tests.py
│
├── nestedserializers/
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

### Author Endpoints

```
GET     /author/
POST    /author/
GET     /author/<id>/
PUT     /author/<id>/
DELETE  /author/<id>/
```

---

### Book Endpoints

```
GET     /book/
POST    /book/
GET     /book/<id>/
PUT     /book/<id>/
DELETE  /book/<id>/
```

---

## 📌 Example Response (Nested Data)

### GET /author/1/

```json
{
  "id": 1,
  "name": "Author One",
  "books": [
    {
      "id": 1,
      "title": "Book One",
      "rating": 5,
      "author": 1
    },
    {
      "id": 2,
      "title": "Book Two",
      "rating": 4,
      "author": 1
    }
  ]
}
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

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

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🧠 Key Concepts Demonstrated

- Nested Serializers in DRF  
- ModelViewSet for rapid API development  
- DefaultRouter for automatic URL routing  
- One-to-many relationships using ForeignKey  
- Clean API structuring and response design  

---

## 🔮 Future Enhancements

- Add authentication (JWT / Token)  
- Pagination & filtering  
- Swagger / OpenAPI documentation  
- Permissions and role-based access control  
- Performance optimization with select_related / prefetch_related  

---

## 👨‍💻 Author

**Aranya Majumdar**

---

## ⭐ Notes

- Uses `ModelViewSet` for both Author and Book APIs  
- Router automatically generates endpoints  
- Nested serializer allows viewing related books inside author response  
- Easily extendable to deeper nested relationships or complex APIs  

---