# Student Management System using Django

A basic Student Management System built using the Django framework. This project demonstrates CRUD (Create, Read, Update, Delete) operations for managing student records.

---

## 📌 Features

- Add a new student
- View all students
- Edit student details
- Delete student records
- Home page navigation
- Django Admin Panel support

---

## 🛠️ Technologies Used

- Python 3
- Django
- HTML
- SQLite3 (Default Django Database)

---

## 📂 Project Structure

```
campus/
│
├── campus/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── student_list.html
│   │   ├── add_student.html
│   │   └── edit_student.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── db.sqlite3
├── manage.py
└── README.md
```

---
## ⚙️ Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Navigate to the project

```bash
cd campus
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

### Activate the virtual environment
```bash
venv\Scripts\activate
```
### Install dependencies

```bash
pip install django
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the development server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/students/
```

---

## 📄 Available Pages

| Page | URL |
|------|-----|
| Home | `/students/` |
| Student List | `/students/list/` |
| Add Student | `/students/add/` |
| Edit Student | `/students/edit/<id>/` |
| Delete Student | `/students/delete/<id>/` |
| Admin Panel | `/admin/` |

---

## 📚 CRUD Operations

### Create
Allows the administrator to add new student records.

### Read
Displays all student details in a table.

### Update
Allows editing existing student information.

### Delete
Removes a student record from the database.