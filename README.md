# 🔗 Tiny URL

**Tiny URL** is a lightweight platform for blog management and subscription plan showcasing. It includes features like user authentication, blog categorization, and tier-based pricing with monthly and annual billing.

---

## ✨ Features

- User Registration & Login (Token Authentication)
- Blog Category CRUD (Admin only)
- Rich blog creation and publishing with image and social URLs
- Dynamic pricing plan structure with link volume and features
- Clean API responses with soft delete mechanism

---

## 🛠 Tech Stack

- **Backend**: Python, Django, Django Rest Framework (DRF)
- **Editor**: CKEditor (Rich Text Uploading)
- **Authentication**: Token Authentication
- **Database**: SQLite (default, development)
- **Media**: Image Upload support (via DRF + CKEditor)

---

## ⚙️ Setup Instructions

1. **Clone the Repository**:
```bash
git clone https://github.com/muhammedshabeen/url-shortner-api.git
cd url-shortner-api
```

2. **Create Virtual Environment and Install Requirements**:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

3. **Apply Migrations and Run Server**:
```bash
python manage.py migrate
python manage.py runserver
```

4. **Admin Panel** (optional):
```bash
python manage.py createsuperuser
```

5. **Database**:
- SQLite is used by default and `db.sqlite3` will be created after migration.
- You may back up or commit it in the repo for demonstration purposes.

---
# 📘 API Specification - Blog and Pricing Platform

## 📦 Authentication

| Method | URL        | Purpose              | Auth Required |
|--------|------------|----------------------|---------------|
| POST   | `/register/` | Register new user and get token   | ❌ No          |
| POST   | `/login/`    | Login and get token  | ❌ No          |

### Sample Requests

**Register**
```json
POST /register/
{
  "username": "shabeen",
  "email": "a@b.com",
  "password": "abc123"
}
```

**Login**
```json
POST /login/
{
  "username": "shabeen",
  "password": "abc123"
}
```

---

## 📚 Blog Category Endpoints

| Method | URL                           | Purpose                | Auth Required     |
|--------|-------------------------------|------------------------|-------------------|
| GET    | `/blog-categories/`           | List all categories    | ✅ Admin Only      |
| POST   | `/blog-categories/`           | Create new category    | ✅ Admin Only      |
| PUT    | `/blog-categories/<pk>/`      | Update category        | ✅ Admin Only      |
| DELETE | `/blog-categories/<pk>/`      | Soft delete category   | ✅ Admin Only      |

---

## 📝 Blog Endpoints

| Method | URL                    | Purpose                    | Auth Required     |
|--------|------------------------|----------------------------|-------------------|
| GET    | `/blogs/`              | List all published blogs   | ❌ No              |
| GET    | `/blogs/?slug=value`  | Retrieve blog by slug      | ❌ No              |
| POST   | `/blogs/`              | Create blog post           | ✅ Admin Only      |
| PUT    | `/blogs/<pk>/`         | Update blog post           | ✅ Admin Only      |
| DELETE | `/blogs/<pk>/`         | Soft delete blog post      | ✅ Admin Only      |

---

## 💸 Plan & Pricing Endpoints

| Method | URL        | Purpose                          | Auth Required |
|--------|------------|----------------------------------|---------------|
| GET    | `/plans/`  | List all plans & pricing tiers   | ❌ No          |

---

## 📦 Sample Responses

**Register Response**
```json
{
  "message": "User registered successfully",
  "token": "abc...",
  "user_detail": {
    "id": 1,
    "username": "shabeen",
    "email": "a@b.com"
  }
}
```

**Blog List Response**
```json
{
  "message": "Blog posts retrieved successfully",
  "data": [
    {
      "title": "Example Title",
      "slug": "example-title",
      "description": "...",
      "published_date": "2024-01-01T00:00:00Z"
    }
  ]
}
```

---

## 🔐 Authentication

All endpoints requiring authentication use **Token-based Auth**. Include the following header:

```
Authorization: Token <your_token>
```
