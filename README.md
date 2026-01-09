📝 Personal Blog Platform (Django)

A Django-based personal blog application that allows users to create, read, and manage blog posts with SEO-friendly slugs, comments, likes, and admin control.

🚀 Features
Create, edit, and delete blog posts
SEO-friendly URLs using slugs
Like system for posts
Comment system
Django Admin panel for easy management
User authentication & permissions
Clean UI with CSS styling

🛠 Technologies Used
Python 3
Django Framework
SQLite Database
HTML, CSS
Django Admin

📂 Project Structure
blog_project/
│
├── blog/
│   ├── migrations/
│   ├── static/
│   │   └── blog/
│   │       └── style.css
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html
│   │       ├── post_list.html
│   │       └── post_detail.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
└── manage.py

⚙️ Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/your-username/blog-project.git

2️⃣ Navigate to project folder
cd blog_project

3️⃣ Install dependencies
pip install django

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Run server
python manage.py runserver


Open browser and visit:
👉 http://127.0.0.1:8000/

🔐 Admin Panel

Access admin dashboard at:
👉 http://127.0.0.1:8000/admin/

Admin can:
Add blog posts
Manage comments
Manage users

🧠 Key Concepts Used

Django MVT architecture
Models & migrations
Template inheritance
Static files handling
Slug-based routing
Authentication & permissions

📌 Future Enhancements

User registration & profile pages
AJAX-based like system
Pagination
Search functionality
Deployment on cloud

👨‍💻 Author

Prathamesh Nivdekar
MCA Student | Python & Django Developer

📄 License

This project is for learning and educational purposes.
