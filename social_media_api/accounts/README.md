🚀 User Authentication & Accounts API (Django + DRF)

This project implements a custom user authentication system using Django and Django REST Framework (DRF).
It supports user registration, login with token-based authentication, and authenticated user profile management.

🧱 Features

Custom user model extending Django’s AbstractUser

Token-based authentication using DRF

User registration & login endpoints

Authenticated profile retrieval and update

Social-ready user model (followers / following)

📦 Tech Stack

Python 3.x

Django

Django REST Framework

DRF Token Authentication

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>
cd <project-folder>

2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


Make sure these are included:

django

djangorestframework

djangorestframework-authtoken

4️⃣ Configure Settings

In settings.py, ensure the following are set:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Run the Server
python manage.py runserver


Server will start at:

http://127.0.0.1:8000/

🔐 Authentication Flow

This API uses token-based authentication.

Once authenticated, include the token in request headers:

Authorization: Token your_token_here

🧑‍💻 API Endpoints
🔸 Register User

POST /api/accounts/register/

Request Body

{
  "username": "peniel",
  "email": "peniel@example.com",
  "password": "strongpassword123",
  "bio": "Computer science student",
}


Response

{
  "token": "abc123...",
  "username": "peniel"
}

🔸 Login User

POST /api/accounts/login/

Request Body

{
  "username": "peniel",
  "password": "strongpassword123"
}


Response

{
  "token": "abc123...",
  "username": "peniel"
}

🔸 Get User Profile (Authenticated)

GET /api/accounts/profile/

Headers

Authorization: Token abc123...


Response

{
  "username": "",
  "email": "peniel@example.com",
  "bio": "Computer science student",
  "profile_picture": null,
  "followers_count": 0,
  "following_count": 0
}

🔸 Update User Profile (Authenticated)

PUT /api/accounts/profile/

{
  "bio": "Cybersecurity & backend enthusiast"
}

🧬 User Model Overview

The project uses a custom user model extending Django’s AbstractUser.

Fields Added
Field	Type	Description
bio	TextField	Short user description
profile_picture	ImageField	Optional profile image
followers	ManyToMany (self)	Users following this user
following	Reverse relation	Users this user follows