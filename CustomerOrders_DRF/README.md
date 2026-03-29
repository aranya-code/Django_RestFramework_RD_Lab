# 📘 Customer Orders API (Django REST Framework)

A production-ready RESTful API built using **Django** and **Django REST Framework (DRF)** to manage customers and their orders. This project demonstrates **nested serializers**, **authentication**, **pagination**, and **search filtering**.

---

## 🚀 Features

- Full CRUD operations for Customers and Orders  
- Nested serializer (Customer → Orders)  
- Authentication using Basic Authentication  
- Permission control (Authenticated users only)  
- Pagination using LimitOffsetPagination  
- Search functionality for customers  
- Scalable architecture using DRF Generic Views  

---

## 🏗️ Project Structure

```
CustomerOrders/
│
├── CustOrders/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── CustomerOrders/
│   ├── urls.py
│
└── manage.py
```

---

## 📦 Tech Stack

- Python  
- Django  
- Django REST Framework  
- Django Filters  


---

## 🌐 API Endpoints

### Customer Endpoints

```
GET     /customer/
POST    /customer/
GET     /customer/<id>
PUT     /customer/<id>
DELETE  /customer/<id>
```

---

### Order Endpoints

```
GET     /order/
POST    /order/
GET     /order/<id>
PUT     /order/<id>
DELETE  /order/<id>
```

---

## 🔐 Authentication & Permissions

- Uses **Basic Authentication**
- Only authenticated users can access customer APIs

```python
authentication_classes = [BasicAuthentication]
permission_classes = [IsAuthenticated]
```

---

## 🔍 Filtering & Search

- Search enabled on:
  - `name`
  - `id`

```python
filter_backends = [filters.SearchFilter]
search_fields = ['name', 'id']
```

---

## 📄 Pagination

- Uses **LimitOffsetPagination**

Example:
```
/customer/?limit=5&offset=10
```

---

## 📌 Example Response (Nested)

### GET /customer/

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "John",
      "phone": "1234567890",
      "orders": [
        {
          "id": 1,
          "product": "Laptop",
          "quantity": 1,
          "customer": 1
        }
      ]
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
pip install django djangorestframework django-filter
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (for authentication)

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

---

## 🧪 Testing the API

Use tools like:
- Postman  
- cURL  
- Browser (for GET requests)  

**Note:** Provide Basic Auth credentials when accessing `/customer/`

---

## 🧠 Key Concepts Demonstrated

- Nested serializers in DRF  
- Generic class-based views  
- Authentication & permission handling  
- Pagination and search filtering  
- One-to-many relationships using ForeignKey  

---

## 🔮 Future Enhancements

- Token/JWT authentication  
- Advanced filtering using DjangoFilterBackend  
- Role-based permissions  
- Swagger/OpenAPI documentation  
- Order status & tracking system  

---

## 👨‍💻 Author

**Aranya Majumdar**

---

## ⭐ Notes

- Customer API is protected with authentication  
- Orders API is currently open (can be secured if needed)  
- Nested serializer allows fetching all customer orders in a single request  
- Easily extendable for real-world e-commerce systems  

---