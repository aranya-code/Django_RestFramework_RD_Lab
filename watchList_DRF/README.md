# 🎬 WatchList API (Django REST Framework)

A feature-rich RESTful API built using **Django** and **Django REST Framework (DRF)** to manage movies, streaming platforms, and user reviews. This project demonstrates **nested serializers**, **custom fields**, **relationships**, and **API design best practices**.

---

## 🚀 Features

- Full CRUD operations for Movies, Platforms, and Reviews  
- Nested serializers:
  - Platform → Movies  
  - Movie → Reviews  
- Custom serializer fields (calculated data)  
- One-to-many relationships using ForeignKey  
- Review system with rating validation (1–10)  
- Clean API structure using APIView and Generic Views  
- Ready for authentication integration  

---

## 🏗️ Project Structure

```
watchList/
│
├── watchApp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│
├── watchList/
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

### 🎬 Movie Endpoints

```
GET     /list/
POST    /list/
GET     /detail/<id>/
PUT     /detail/<id>/
DELETE  /detail/<id>/
```

---

### 📺 Platform Endpoints

```
GET     /platform/
POST    /platform/
```

---

### ⭐ Review Endpoints

```
GET     /review/
POST    /review/
```

---

## 📌 Example Response (Nested)

### GET /detail/1/

```json
{
  "id": 1,
  "name": "Inception",
  "description": "Sci-fi movie",
  "status": true,
  "streamingplatform": 1,
  "len_obj": 9,
  "Reviews": [
    {
      "id": 1,
      "reviewer": "testuser",
      "rating": 8,
      "description": "Great movie",
      "movielist": 1
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

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

---

## 🧪 Testing

```bash
python manage.py test
```

---

## 🧠 Key Concepts Demonstrated

- Nested serializers in DRF  
- SerializerMethodField (custom computed fields)  
- APIView and GenericAPIView usage  
- Model relationships (ForeignKey)  
- Data validation (rating constraints)  
- Clean API architecture  

---

## 🔮 Future Enhancements

- JWT Authentication  
- Permissions (Admin vs User roles)  
- Pagination & filtering  
- Swagger/OpenAPI documentation  
- Like/Watchlist feature  
- Review ownership validation  

---

## 👨‍💻 Author

**Aranya Majumdar**

---

## ⭐ Notes

- Nested relationships allow efficient data retrieval  
- Easily extendable to OTT platforms or recommendation systems  
- Good foundation for real-world streaming applications  

---