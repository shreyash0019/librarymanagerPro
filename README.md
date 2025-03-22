# 📚 Libmanage - Library Management System

A simple web-based **Library Management System** built using **Django, MySQL, HTML, CSS, and JavaScript** for efficient book management and borrowing.

## 🚀 Features

- 🔐 **User Authentication** – Separate login for students and admins  
- 📖 **Book Management** – Admins can **add, edit, delete, and view books**  
- 📚 **Borrowing System** – Students can **borrow and return books**  
- 🎨 **Responsive UI** – Clean and user-friendly design  
- 🗄️ **Database Integration** – Uses **MySQL** for data storage  
- ⚡ **REST API Support** – Full CRUD operations with Django REST Framework  

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework (DRF), Python  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** MySQL  
- **API Support:** Django REST Framework  

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

7️⃣ Create a superuser (admin):
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
| `GET` | `/api/books/` | Get all books |
| `POST` | `/api/books/` | Add a new book |
| `GET` | `/api/books/<id>/` | Get book details |
| `PUT` | `/api/books/<id>/` | Update book details |
| `DELETE` | `/api/books/<id>/` | Delete a book |
| `GET` | `/api/students/` | Get all students |
| `POST` | `/api/students/` | Add a new student |
| `GET` | `/api/borrowed-books/` | Get borrowed books |
| `POST` | `/api/borrowed-books/` | Borrow a book |
| `PUT` | `/api/borrowed-books/<id>/` | Update return status |
| `DELETE` | `/api/borrowed-books/<id>/` | Delete a borrowed book record |



## 🎯 Future Improvements
🚀 Add **pagination** in book listings  
🚀 Implement **JWT authentication** for better security  
🚀 Improve **book return tracking** with due dates  

## 🛠 Contributing
Want to contribute? Feel free to **fork the repository**, create a new branch, and submit a **pull request (PR)**.  

## 📜 License
This project is **MIT licensed**.  
