# 🏏 Cricket ScoreCard API (Django REST Framework)

A RESTful API built using **Django REST Framework (DRF)** to manage cricket player scorecards.
This project supports full CRUD operations along with validation, custom responses, and partial updates.

---

## 🚀 Features

* ✅ Add player scorecard
* ✅ List all players
* ✅ Get player details by jersey number
* ✅ Update player stats (partial update supported)
* ✅ Delete player from squad
* ✅ Custom error handling
* ✅ Field validation using serializers
* ✅ Clean API structure using APIView

---

## 🧠 Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* SQLite (default)

---

## 📁 Project Structure

```
cricket/
│── models.py
│── serializers.py
│── views.py
│── urls.py
│── migrations/
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create virtual environment

```
python -m venv env
env\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install django djangorestframework
```

### 4. Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run server

```
python manage.py runserver
```

---

## 📌 API Endpoints

### 🔹 1. Add Player

**POST** `/score/add/`

```
{
  "player_name": "Virat Kohli",
  "jersey_no": 18,
  "technical_skill": "batter"
}
```

---

### 🔹 2. List Players

**GET** `/score/list/`

* Returns all players
* If empty → `"match not started yet"` (400)

---

### 🔹 3. Get Player Detail

**GET** `/score/detail/<jersey_no>`

* Returns player details
* If not found → `"jersey number invalid"` (404)

---

### 🔹 4. Update Player (Partial Update Supported)

**PUT** `/score/update/<jersey_no>`

```
{
  "runs": 82,
  "status": "Out"
}
```

* Only provided fields are updated

---

### 🔹 5. Delete Player

**DELETE** `/score/delete/<jersey_no>`

* Deletes player from squad
* If not found → `"player not in current squad"` (404)

---

## 🧩 Model Fields

| Field           | Type        | Description               |
| --------------- | ----------- | ------------------------- |
| id              | Integer     | Primary key               |
| player_name     | CharField   | Player name               |
| jersey_no       | Integer     | Unique jersey number      |
| technical_skill | ChoiceField | batter, bowler, ar, wk, c |
| runs            | Integer     | Default = 0               |
| wickets         | Integer     | Default = 0               |
| catches         | Integer     | Default = 0               |
| status          | CharField   | Default = "Not Out"       |

---

## ⚠️ Important Notes

* `jersey_no` is used as the unique identifier (not `id`)
* Partial updates are enabled using `partial=True`
* Custom error responses are implemented as per requirements
* Proper HTTP status codes are used

---

## 📦 Best Practices Followed

* Clean separation of logic
* Proper exception handling
* DRF serializer validation
* RESTful API design
* Consistent response structure

---

## 📌 Future Improvements

* Add authentication (JWT)
* Use ViewSets for better structure
* Add pagination & filtering
* Add unit tests

---

## 👨‍💻 Author

**Aranya Majumdar**

---

