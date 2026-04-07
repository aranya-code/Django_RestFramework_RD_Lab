# 📦 Inventory Management API (Django REST Framework)

A lightweight and scalable RESTful API for managing inventory items, built using Django and Django REST Framework. This project supports full CRUD operations, filtering, and sorting capabilities.

---

## 🚀 Features

* ✅ Create, Read, Update, Delete (CRUD) inventory items
* 🔍 Filter items by category
* 📊 Sort items by price (descending)
* ⚡ Fast and simple REST API using ViewSets & APIViews
* 🔐 Unique barcode enforcement
* 🧱 Clean and modular architecture

---

## 🏗️ Tech Stack

* **Backend:** Python, Django
* **API Framework:** Django REST Framework
* **Database:** SQLite (default, configurable)

---

## 📁 Project Structure

```
Inventory/
│── InventoryAPI/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│── Inventory/
│   ├── urls.py
│── manage.py
```

---

## 🧾 Model

The core model used in this project:

* **Inventory** 

Fields:

* `id` (AutoField)
* `name` (CharField)
* `category` (CharField)
* `price` (IntegerField)
* `quantity` (IntegerField)
* `barcode` (Unique IntegerField)

---

## 🔌 API Endpoints

### 🔹 Base Routes (ViewSet)

Defined using router in 

| Method | Endpoint                 | Description     |
| ------ | ------------------------ | --------------- |
| GET    | `/inventory/items/`      | List all items  |
| POST   | `/inventory/items/`      | Create new item |
| PUT    | `/inventory/items/{id}/` | Update item     |
| DELETE | `/inventory/items/{id}/` | Delete item     |

---

### 🔹 Custom Endpoints

#### 📂 Get Items by Category

```
GET /items/query/{category}/
```

Returns all items filtered by category.

---

#### 💰 Get Items Sorted by Price

```
GET /items/sort/
```

Returns all items sorted by price (descending).

---

## 🧠 API Logic Overview

* **ViewSet (ItemViewSet)** 
  Handles:

  * `list()`
  * `create()`
  * `update()`
  * `destroy()`

* **Custom APIs**

  * `ItemByCategory` → Filters items
  * `ItemSorted` → Sorts items by price

* **Serializer** 

  * Converts model instances ↔ JSON

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/amajumdar/inventory_drf.git
cd inventory_drf_
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install django djangorestframework
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start server

```bash
python manage.py runserver
```

---

## 🧪 Example Request

### Create Item

```json
POST /inventory/items/

{
    "name": "Laptop",
    "category": "Electronics",
    "price": 50000,
    "quantity": 10,
    "barcode": 123456
}
```

---

## 📌 Response Example

```json
{
    "id": 1,
    "name": "Laptop",
    "category": "Electronics",
    "price": 50000,
    "quantity": 10,
    "barcode": 123456
}
```

---

## ⚠️ Error Handling

* Returns `400 Bad Request` for invalid data
* Returns `404 Not Found` for missing items
* Enforces unique barcode constraint

---

## 🔮 Future Improvements

* 🔐 Authentication & Authorization (JWT)
* 🔎 Search & pagination
* 📦 Bulk upload support
* 🧾 Swagger/OpenAPI documentation
* 🗄️ PostgreSQL integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.


---

## 👨‍💻 Author

**Aranya Majumdar**

---
