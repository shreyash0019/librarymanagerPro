# 📚 Libmanage - Library Management System

A **Library Management System** built using **Django and MySQL** to efficiently manage book records and borrowing. This project is part of a machine test assignment for the Python Django Developer position at **Keywordio**.

## 🚀 Features

### 🔐 Admin Operations
- **Signup** – Create a new admin account (email must be unique)
- **Login** – Admin login using email and password
- **Book Management**
  - **Create** – Add new books
  - **Read** – Retrieve all books
  - **Update** – Modify book details
  - **Delete** – Remove a book record

### 📚 Student View
- View the list of all books (read-only access)

### 🔧 Technical Specifications
- **Framework:** Django (Specify version)
- **API:** Django REST Framework (DRF) for RESTful endpoints
- **Database:** MySQL
- **Authentication:** Token-based authentication for admin endpoints
- **Error Handling:** Proper HTTP status codes and messages for invalid input
- **Optional UI:** Django templates or any frontend framework (ReactJS, Angular)

## 📁 Project Structure
```
Libmanage/
│── library/                # Main Django app
│   │── migrations/         # Database migrations
│   │── models.py           # Database models
│   │── serializers.py      # DRF serializers
│   │── views.py            # API views
│   │── urls.py             # URL routes
│── librarymanagerpro.postman_collection.json  # API testing collection
│── requirements.txt        # Python dependencies
│── manage.py               # Django management script
│── settings.py             # Project settings
│── README.md               # Project documentation
│── .hintrc                 # Linting configuration
│── MIT License             # License file
```

## ⚙️ Installation

1️⃣ Clone the repository:
```sh
git clone https://github.com/shreyash0019/librarymanagerPro.git
```

2️⃣ Navigate to the project directory:
```sh
cd librarymanagerPro
```

3️⃣ Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

4️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

5️⃣ Set up MySQL Database:
- Create a database (`library_db`)
- Update **`settings.py`** with MySQL credentials:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'library_db',
          'USER': 'your_mysql_user',
          'PASSWORD': 'your_mysql_password',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```

6️⃣ Apply database migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

7️⃣ Create an admin user:
```sh
python manage.py createsuperuser
```

8️⃣ Run the development server:
```sh
python manage.py runserver
```

9️⃣ Open the app in your browser:
```
http://127.0.0.1:8000/
```

## 🔥 API Endpoints (Django REST Framework)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/admin/signup/` | Register a new admin |
| `POST` | `/api/admin/login/` | Admin login |
| `POST` | `/api/books/` | Add a new book (Admin) |
| `GET` | `/api/books/` | Get all books |
| `GET` | `/api/books/<id>/` | Get book details |
| `PUT` | `/api/books/<id>/` | Update book details (Admin) |
| `DELETE` | `/api/books/<id>/` | Delete a book (Admin) |

## 🎯 Future Improvements
- 🔹 Implement **pagination** for book listings
- 🔹 Add **JWT authentication**
- 🔹 Track **book return dates** and notifications

## 🤝 Contribution
Fork the repository, create a new branch, and submit a **pull request (PR)**.

## 🛡️ License
This project is licensed under the **MIT License**.
See the [LICENSE](https://github.com/shreyash0019/librarymanagerPro/blob/master/MIT%20License) file for details.

