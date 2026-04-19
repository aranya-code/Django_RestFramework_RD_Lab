# 🎯 Wish API (Django REST FRAMEWORK)

A simple RESTful API built using Django and Django REST Framework to create, retrieve, update, and delete wishes.

---

## 🚀 Features

* Create a new wish
* Retrieve all wishes
* Retrieve a specific wish by ID
* Update an existing wish
* Delete a wish
* Fully tested endpoints

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default DB)

---

## 📂 Project Structure

```
wishApp/
│
├── models.py        # Wish model definition
├── serializers.py   # Serializer for Wish model
├── views.py         # API logic (CRUD operations)
├── urls.py          # URL routing
├── tests.py         # Unit tests for API
```

---

## 🧩 Model

The core model is:

* **Wish**

  * `created` (DateTime)
  * `title` (optional)
  * `wishtext` (required)

Defined in: 

---

## 🔄 API Endpoints

### 📌 Base URL

```
/wishes/
```

### 1. Get All Wishes

* **GET** `/wishes/`
* Returns list of all wishes

### 2. Create a Wish

* **POST** `/wishes/`

```json
{
  "title": "Birthday",
  "wishtext": "Happy Birthday!"
}
```

---

### 3. Get Single Wish

* **GET** `/wishes/<id>/`

---

### 4. Update a Wish

* **PUT** `/wishes/<id>/`

```json
{
  "title": "Updated Title",
  "wishtext": "Updated message"
}
```

---

### 5. Delete a Wish

* **DELETE** `/wishes/<id>/`

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create virtual environment

```bash
python -m venv venv
On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start server

```bash
python manage.py runserver
```

---

## 🧪 Running Tests

Run all tests using:

```bash
python manage.py test
```

Test cases include:

* Fetch all wishes
* Create valid/invalid wishes
* Retrieve single/non-existent wish
* Update with valid/invalid data
* Delete a wish

Defined in: 

---

## 🔧 Implementation Details

* **Serializer** converts model instances to JSON and validates input
  Defined in: 

* **Views** use function-based logic for handling HTTP methods
  Defined in: 

* **URL Routing** connects endpoints to views
  Defined in: 

---

## ⚠️ Notes

* CSRF is disabled for simplicity (`@csrf_exempt`)
* Uses function-based views instead of class-based views
* Returns proper HTTP status codes (200, 201, 400, 404, 204)

---

## 📌 Future Improvements

* Add authentication (JWT / Token-based)
* Switch to class-based views or ViewSets
* Add pagination
* Add filtering & search
* Improve validation rules

---

## 👨‍💻 Author

**Aranya Majumdar**

---

