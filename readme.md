# 🚀 Mini Task Management System API

## 📌 Project Overview

This is a backend API built using **FastAPI** for managing tasks, projects, users, and comments.
It includes authentication, role-based authorization, relational database handling, and business logic separation.

---

## 🎯 Features

* ✅ User Registration & Login (JWT Authentication)
* ✅ Role-Based Access Control (Admin, Manager, Employee)
* ✅ Project Management (Create, View)
* ✅ Task Management (Assign, Update Status)
* ✅ Comment System (Max 3 comments per user per task)
* ✅ Soft Delete & Hard Delete (Role-Based)
* ✅ Database Relationships (One-to-Many)
* ✅ Clean Architecture (Routes + Services)

---

## 👤 Roles & Permissions

| Role         | Permissions                                   |
| ------------ | --------------------------------------------- |
| **Admin**    | Full access, Hard delete comments             |
| **Manager**  | Manage projects & tasks, Soft delete comments |
| **Employee** | View assigned tasks, Add comments             |

---

## 🧠 Business Logic Implemented

* 🔹 A user can comment **only 3 times per task**
* 🔹 Manager performs **Soft Delete** (`is_deleted = True`)
* 🔹 Admin performs **Hard Delete** (permanent removal)
* 🔹 Email is **unique**
* 🔹 Role-based access using dependencies

---

## 🗄️ Database Design

### Entities:

* **Users**
* **Projects**
* **Tasks**
* **Comments**

### Relationships:

* User → Projects (One-to-Many)
* Project → Tasks (One-to-Many)
* Task → Comments (One-to-Many)
* User → Tasks (Assigned)

---

## 🔗 Advanced Concepts Used

* 🔐 JWT Authentication
* 🛡 Role-Based Authorization
* 🔁 Cascade Delete & Set Null
* 🧠 ORM (SQLAlchemy)
* 📦 Pydantic Validation
* 🧩 Layered Architecture (Routes & Services)

---

## 📁 Project Structure

```
app/
│── main.py
│── database.py
│
│── models/
│── schemas/
│── services/
│── routers/
│── auth/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd task-management
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

👉 Interactive Swagger UI available

---

## 🧪 Testing APIs (Postman / Swagger)

1. Register user
2. Login → Get JWT token
3. Authorize using Bearer Token
4. Access protected endpoints

---

## 🐳 Docker Setup

### Build Image

```bash
docker build -t mini-task-management-api .
```

### Run Container

```bash
docker run -d -p 8000:8000 mini-task-management-api
```

---

## ⚠️ Important Notes

* Delete `test.db` after model changes
* Ensure `__init__.py` exists in all folders
* Always run server from root directory

---

## 💡 Future Improvements

* Pagination & Filtering
* Unit Testing
* Logging System
* PostgreSQL Integration
* Deployment (Render / Railway)

---

## 🎤 Interview Highlights

* Used **layered architecture**
* Implemented **role-based access control**
* Handled **edge cases (comment limit, soft delete)**
* Applied **database relationships & constraints**

---

## 👨‍💻 Author

**Eshaa Naeem**

---

## ⭐ Final Note

This project demonstrates backend development skills including API design, authentication, database management, and clean code practices.
