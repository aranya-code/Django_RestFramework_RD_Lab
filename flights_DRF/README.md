# ✈️ Flight Reservation API (Django REST Framework)

A RESTful backend system for managing flights, passengers, and reservations built using **Django** and **Django REST Framework (DRF)**. This project supports authentication, flight search, and reservation creation.

---

## 🚀 Features

* Flight management (CRUD APIs)
* Passenger management
* Reservation system (Flight + Passenger mapping)
* Flight search API
* Token-based authentication
* MySQL database integration
* Input validation for flight numbers

---

## 🏗️ Tech Stack

* Python 3.x
* Django 5.x
* Django REST Framework
* MySQL
* Token Authentication (DRF)

---

## 📁 Project Structure

```
flights/
│
├── flightApp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── flights/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## 🧩 Models

Defined in 

* **Flight**

  * flightNumber
  * airlines
  * departureCity
  * arrivalCity
  * departureDate
  * departureTime

* **Passenger**

  * name
  * email
  * phone

* **Reservation**

  * One-to-One with Passenger
  * Foreign Key to Flight

* Auto token generation for users using Django signals

---

## 🔄 Serializers

Defined in 

* `FlightSerializer`

  * Includes validation for alphanumeric flight numbers
* `PassengerSerializer`
* `ReservationSerializer`

---

## 🌐 API Endpoints

Defined in 

### 🔹 ViewSets (CRUD)

| Endpoint         | Method    | Description         |
| ---------------- | --------- | ------------------- |
| `/flights/`      | GET, POST | Manage flights      |
| `/passengers/`   | GET, POST | Manage passengers   |
| `/reservations/` | GET, POST | Manage reservations |

---

### 🔹 Custom APIs

Defined in 

#### 🔍 Find Flights

```
POST /flights/findflights
```

**Request Body:**

```json
{
  "departureCity": "NYC",
  "arrivalCity": "LA",
  "departureDate": "2025-01-01"
}
```

---

#### 💾 Save Reservation

```
POST /save_reservations
```

**Request Body:**

```json
{
  "flightNumber": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890"
}
```

---

### 🔐 Authentication

```
POST /api-token-auth/
```

Returns authentication token.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install django djangorestframework mysqlclient python-dotenv
```

---

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔑 Authentication Usage

Add token to headers:

```
Authorization: Token <your_token>
```

---


## 📌 Future Enhancements

* Booking history
* Payment integration
* JWT authentication
* Swagger/OpenAPI docs
* Docker support

---

## 👨‍💻 Author

Aranya Majumdar

---

## 📄 License

This project is for learning/demo purposes.
