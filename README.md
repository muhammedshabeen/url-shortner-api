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
    "email": "a@b.com",
    "password" : "123"
  }
}
```

**Blog List Response**
```json
{
    "message": "Blog posts retrieved successfully",
    "data": [
        {
            "id": 2,
            "title": "How To Sell on Instagram in 2025: The Complete Guide",
            "slug": "how-to-sell-on-instagram-in-2025-the-complete-guide",
            "description": "It pays to know what you’re doing when you sell on Instagram, whether directly on the platform or",
            "featured_image": "/media/blog_images/Harry_Potter_and_the_Sorcerers_Stone_qcEYfzJ.jpg",
            "category_detail": {
                "id": 2,
                "created_at": "2025-06-25T18:26:24.408143+05:30",
                "updated_at": "2025-06-25T18:26:24.408143+05:30",
                "soft_delete": false,
                "title": "Marketing Channels & Strategies",
                "slug": "marketing-channels-strategies",
                "created_by": 1
            }
        }
    ]
}
```


**Blog Detail Response**
```json
{
    "message": "Blog posts retrieved successfully",
    "data": {
        "id": 2,
        "category_detail": {
            "id": 2,
            "created_at": "2025-06-25T18:26:24.408143+05:30",
            "updated_at": "2025-06-25T18:26:24.408143+05:30",
            "soft_delete": false,
            "title": "Marketing Channels & Strategies",
            "slug": "marketing-channels-strategies",
            "created_by": 1
        },
        "created_at": "2025-06-26T12:30:15.047667+05:30",
        "updated_at": "2025-06-26T12:34:25.881292+05:30",
        "soft_delete": false,
        "title": "How To Sell on Instagram in 2025: The Complete Guide",
        "slug": "how-to-sell-on-instagram-in-2025-the-complete-guide",
        "author_name": "John Doe",
        "description": "It pays to know what you’re doing when you sell on Instagram, whether directly on the platform or",
        "featured_image": "/media/blog_images/Harry_Potter_and_the_Sorcerers_Stone_qcEYfzJ.jpg",
        "content": "<h2>Main Takeaways From This Article</h2>\r\n\r\n<ul>\r\n\t<li>Explore seven leading affiliate marketing programs and how beginner-friendly they are.</li>\r\n\t<li>Analyze each affiliate marketing platform based on its overview, commission rate, payment methods, cookie duration, and ideal user base.</li>\r\n\t<li>There are a few things you should consider while picking the best affiliate marketing program to meet your unique needs. Also, keep an eye on anticipated future trends to stay up to date.</li>\r\n\t<li>Learn how TinyURL, with its advanced link management tools, can enhance your affiliate marketing efforts, particularly for those newly entering the field.</li>\r\n\t<li>Choosing the right affiliating marketing program as a beginner could potentially set the stage for your success. Make it the finish line, not the starting point.</li>\r\n</ul>\r\n\r\n<h2>What Is an Affiliate Program?</h2>\r\n\r\n<p>An affiliate program is a digital marketing strategy where businesses offer financial rewards to partners (affiliates) for bringing in new customers or traffic.</p>\r\n\r\n<p>&nbsp;</p>",
        "published_date": "2025-06-26T12:30:15.050998+05:30",
        "fb_url": "https://facebook.com/",
        "twitter_url": "https://twitter.com/",
        "linkedin_url": "https://linkedin.com/",
        "is_published": true,
        "created_by": 1,
        "category": 2
    }
}
```
**Plan Pricing Detail Response**
```json
{
    "message": "Successfully retrieved plans",
    "data": [
        {
            "plan": "Free",
            "tiers": {
                "annual": [
                    {
                        "link_volume": "Free",
                        "billing_cycle": "annual",
                        "price": "0.00",
                        "annual_equivalent_price": "0.00",
                        "features": [
                            {
                                "feature_name": "Links with Unlimited Trackable Clicks",
                                "feature_category": "Monthly Volumes",
                                "value": "X"
                            },
                            {
                                "feature_name": "Click Analytics on All Other Links",
                                "feature_category": "Monthly Volumes",
                                "value": "X"
                            },
                            {
                                "feature_name": "Branded Links",
                                "feature_category": "Monthly Volumes",
                                "value": "30"
                            },
                            {
                                "feature_name": "Link Shortening Limit",
                                "feature_category": "Monthly Volumes",
                                "value": "100"
                            }
                        ]
                    }
                ],
                "monthly": [
                    {
                        "link_volume": "Free",
                        "billing_cycle": "monthly",
                        "price": "0.00",
                        "annual_equivalent_price": "0.00",
                        "features": [
                            {
                                "feature_name": "Links with Unlimited Trackable Clicks",
                                "feature_category": "Monthly Volumes",
                                "value": "X"
                            },
                            {
                                "feature_name": "Click Analytics on All Other Links",
                                "feature_category": "Monthly Volumes",
                                "value": "X"
                            },
                            {
                                "feature_name": "Branded Links",
                                "feature_category": "Monthly Volumes",
                                "value": "30"
                            },
                            {
                                "feature_name": "Link Shortening Limit",
                                "feature_category": "Monthly Volumes",
                                "value": "100"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "plan": "Pro",
            "tiers": {
                "annual": [
                    {
                        "link_volume": "500",
                        "billing_cycle": "annual",
                        "price": "9.99",
                        "annual_equivalent_price": "119.88",
                        "features": [
                            {
                                "feature_name": "Links with Unlimited Trackable Clicks",
                                "feature_category": "Monthly Volumes",
                                "value": "500"
                            },
                            {
                                "feature_name": "Click Analytics on All Other Links",
                                "feature_category": "Monthly Volumes",
                                "value": "9,500"
                            },
                            {
                                "feature_name": "Branded Links",
                                "feature_category": "Monthly Volumes",
                                "value": "10,000"
                            },
                            {
                                "feature_name": "Link Shortening Limit",
                                "feature_category": "Monthly Volumes",
                                "value": "10,000"
                            }
                        ]
                    },
                    {
                        "link_volume": "5k",
                        "billing_cycle": "annual",
                        "price": "29.00",
                        "annual_equivalent_price": "348.00",
                        "features": [
                            {
                                "feature_name": "Links with Unlimited Trackable Clicks",
                                "feature_category": "Monthly Volumes",
                                "value": "5,000"
                            },
                            {
                                "feature_name": "Click Analytics on All Other Links",
                                "feature_category": "Monthly Volumes",
                                "value": "35,000"
                            },
                            {
                                "feature_name": "Branded Links",
                                "feature_category": "Monthly Volumes",
                                "value": "40,000"
                            },
                            {
                                "feature_name": "Link Shortening Limit",
                                "feature_category": "Monthly Volumes",
                                "value": "40,000"
                            }
                        ]
                    },
                    {
                        "link_volume": "50k",
                        "billing_cycle": "annual",
                        "price": "199.00",
                        "annual_equivalent_price": "2388.00",
                        "features": [
                            {
                                "feature_name": "Links with Unlimited Trackable Clicks",
                                "feature_category": "Monthly Volumes",
                                "value": "50,000"
                            },
                            {
                                "feature_name": "Click Analytics on All Other Links",
                                "feature_category": "Monthly Volumes",
                                "value": "200,000"
                            },
                            {
                                "feature_name": "Branded Links",
                                "feature_category": "Monthly Volumes",
                                "value": "250,000"
                            },
                            {
                                "feature_name": "Link Shortening Limit",
                                "feature_category": "Monthly Volumes",
                                "value": "250,000"
                            }
                        ]
                    }
                ],
                "monthly": [
                    {
                        "link_volume": "500",
                        "billing_cycle": "monthly",
                        "price": "12.99",
                        "annual_equivalent_price": "0.00",
                        "features": [
                            {
                                "feature_name": "Links with Unlimited Trackable Clicks",
                                "feature_category": "Monthly Volumes",
                                "value": "500"
                            },
                            {
                                "feature_name": "Click Analytics on All Other Links",
                                "feature_category": "Monthly Volumes",
                                "value": "9,500"
                            },
                            {
                                "feature_name": "Branded Links",
                                "feature_category": "Monthly Volumes",
                                "value": "10,000"
                            },
                            {
                                "feature_name": "Link Shortening Limit",
                                "feature_category": "Monthly Volumes",
                                "value": "10,000"
                            },
                            {
                                "feature_name": "Click Analytics on All Other Links",
                                "feature_category": "Monthly Volumes",
                                "value": "35,000"
                            }
                        ]
                    },
                    {
                        "link_volume": "5k",
                        "billing_cycle": "monthly",
                        "price": "35.00",
                        "annual_equivalent_price": "0.00",
                        "features": [
                            {
                                "feature_name": "Links with Unlimited Trackable Clicks",
                                "feature_category": "Monthly Volumes",
                                "value": "5,000"
                            },
                            {
                                "feature_name": "Branded Links",
                                "feature_category": "Monthly Volumes",
                                "value": "40,000"
                            },
                            {
                                "feature_name": "Link Shortening Limit",
                                "feature_category": "Monthly Volumes",
                                "value": "40,000"
                            }
                        ]
                    },
                    {
                        "link_volume": "50k",
                        "billing_cycle": "monthly",
                        "price": "249.00",
                        "annual_equivalent_price": "0.00",
                        "features": [
                            {
                                "feature_name": "Links with Unlimited Trackable Clicks",
                                "feature_category": "Monthly Volumes",
                                "value": "50,000"
                            },
                            {
                                "feature_name": "Click Analytics on All Other Links",
                                "feature_category": "Monthly Volumes",
                                "value": "200,000"
                            },
                            {
                                "feature_name": "Branded Links",
                                "feature_category": "Monthly Volumes",
                                "value": "250,000"
                            },
                            {
                                "feature_name": "Link Shortening Limit",
                                "feature_category": "Monthly Volumes",
                                "value": "250,000"
                            }
                        ]
                    }
                ]
            }
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
