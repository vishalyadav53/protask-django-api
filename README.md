# 🚀 Task Management REST API (Production-Ready)

A fully-secured, optimized, and automated-tested Task Management Backend API built using **Django REST Framework (DRF)** and **Python**. This project follows professional industry standards, implementing JWT Authentication, Query Optimization, and robust Unit Testing.

🎯 **Live Demo:** [Interactive Swagger UI Documentation](https://protask-django-api.onrender.com/swagger/)

---

## 🔥 Core Features & Key Highlights

* **🔒 JWT Token Authentication:** Implemented secure user login and session management using `SimpleJWT` (handling both Access and Refresh tokens).
* **👥 User Registration & Management:** Created a dedicated self-registration endpoint (`/register/`) that securely hashes and encrypts user passwords before saving them to the database.
* **🛡️ Row-Level Security:** Overrode `get_queryset` in views to enforce strict isolation—logged-in users can only access, modify, or delete their own tasks.
* **⚡ Query Optimization (Search, Filter & Pagination):** Engineered global pagination, dynamic filtering on `is_completed`, and global search functionality on `title` and `description` to efficiently handle heavy database traffic.
* **🧪 Automated Unit Testing:** Developed comprehensive test coverage using `APITestCase` scripts to automatically validate inputs, custom character validations, security blocks, and search features.
* **📖 Live API Documentation:** Integrated **Swagger UI** (`drf-yasg`) for seamless API testing, interactive visualization, and frontend integration.

---

## 🛠️ Tech Stack Used

* **Backend Framework:** Django & Django REST Framework (DRF)
* **Database:** SQLite3 (Development)
* **Security & Auth:** Rest Framework SimpleJWT (Bearer Tokens)
* **Documentation Tool:** Swagger UI (`drf-yasg`)
* **Testing Suite:** DRF Testing Tools (`APITestCase`)

---

## 🚀 Installation & Setup Guide

Follow these steps to set up and run the project locally on your system:

### 1. Clone the Repository
```bash
git clone [https://github.com/vishalyadav53/protask-django-api.git](https://github.com/vishalyadav53/protask-django-api.git)
cd protask-django-api