# 🚀 Automated Job Application System

## 📌 Project Overview

The **Automated Job Application System** is a web-based application developed using **Python (Flask)** that helps users search, filter, and apply for jobs from a predefined dataset.
The system also includes **user authentication**, **job application tracking**, and a **trust score mechanism** to prevent fake or spam users.

This project demonstrates how multiple technologies (backend, frontend, database) work together in a real-world application.

---

## 🎯 Objectives

* Provide a centralized platform for job listings
* Allow users to register and log in securely
* Enable users to apply for jobs easily
* Track job applications per user
* Calculate a trust score for users based on their activity
* Prevent fake or suspicious users from abusing the system

---

## 🛠️ Tech Stack Used

### 🔹 Backend

* **Python 3**
* **Flask** (Web Framework)
* **SQLite** (Database)

### 🔹 Frontend

* **HTML5**
* **CSS3** (Dark theme UI)
* **JavaScript**

### 🔹 Libraries & Tools

* Flask
* Pandas
* SQLite3
* Werkzeug (for password hashing)

---

## 📂 Project Folder Structure

```
AutomatedJobApplicationSystem/
│
├── app.py                  # Main Flask application
├── config.py               # Secret key & database path
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation
│
├── database/
│   ├── database.db         # SQLite database (auto-created)
│   └── init_db.py          # Database table creation
│
├── data/
│   └── jobs_dataset.csv    # Sample job data
│
├── backend/
│   ├── __init__.py
│   ├── auth.py             # Login & registration logic
│   ├── jobs.py             # Job filtering & apply logic
│   └── trust_score.py      # User trust score calculation
│
├── frontend/
│   ├── templates/          # HTML templates
│   └── static/             # CSS & JavaScript
│
└── .gitignore
```

---

## 🗄️ Database Design

### 🔹 Users Table

* id
* username
* password (hashed)
* trust_score

### 🔹 Applications Table

* id
* user_id
* job_id
* applied_date

---

## ⚙️ Setup Instructions

### 1️⃣ Clone or Download Project

```bash
git clone <project-repo-url>
cd AutomatedJobApplicationSystem
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4️⃣ Initialize Database (Run Once)

```bash
python -m database.init_db
```

You should see:

```
Database tables created successfully!
```

---

## ▶️ Running the Application

```bash
python app.py
```

Open browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🧪 Sample User Flow

1. User registers with username & password
2. User logs into the system
3. Dashboard displays available jobs
4. User applies for a job
5. Application is stored in database
6. Trust score updates automatically

---

## 🔐 Security Features

* Password hashing using Werkzeug
* Session-based authentication
* Trust score system to prevent fake users
* Input validation to avoid misuse

---

## 🌟 Key Features

* User Registration & Login
* Job Listing from CSV Dataset
* Job Application Tracking
* Trust Score Calculation
* Clean Dark Theme UI
* Modular & Scalable Code Structure

---

## 🎓 Academic Relevance

This project is suitable for:

* **Mini Project**
* **Final Year Project**
* **Web Development Practicals**
* **Flask / Python Viva**

It demonstrates:

* MVC architecture
* Backend-Frontend integration
* Database connectivity
* Real-world application flow

---

## 📌 Future Enhancements

* Admin dashboard
* Resume upload feature
* Real job portal API integration
* Email notifications
* Auto-apply using AI filters

---

## 👩‍💻 Developed By

**Name:** Varshitha
**Course:** Software Engineering
**Project Type:** Academic / Learning Project

---

## ✅ Conclusion

The **Automated Job Application System** successfully integrates backend logic, frontend UI, and database operations into a complete, functional web application.
It serves as a strong foundation for real-world job portal systems and academic evaluations.
