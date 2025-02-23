# 📝 Django To-Do App ✅  

A simple and efficient task management application built with Django. It allows users to create, edit, delete, and mark tasks as complete. Additionally, it supports task sorting and email notifications upon task completion.  

## 🚀 Features  
✅ **User-friendly task management** – Add, edit, and delete tasks easily.  
✅ **Sorting functionality** – Sort tasks by priority and due date.  
✅ **Mark tasks as complete** – Helps track progress efficiently.  
✅ **Email notifications** – Sends an email when a task is marked as complete.  
✅ **Soft delete** – Deleted tasks are not permanently removed, allowing for recovery.  
✅ **Bootstrap-powered UI** – Clean and responsive interface for a better experience.  

---

## 🛠️ Setup Instructions  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/vivekso/todo.git
cd todo
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create a Superuser (For Admin Panel)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a superuser account.

### **6️⃣ Start the Development Server**  
```bash
python manage.py runserver
```
Now, visit **http://127.0.0.1:8000/** in your browser to use the app.

---

## 📧 Email Notifications Setup  

This app sends an email when a task is marked as complete. To enable this, configure your email settings in `settings.py`:  

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```
📌 **Note:** Enable "Less Secure Apps" for your Gmail account or use an App Password if you have 2FA enabled.


## 🏗️ Project Structure  
```
todo/
│── tasks/                # Main Django app for task management
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates for views
│   ├── static/           # Static files (CSS, JS)
│   ├── views.py          # Business logic for task operations
│   ├── models.py         # Database models
│   ├── urls.py           # URL routing
│   ├── forms.py          # Django forms for task input
│── todo_project/         # Main project settings
│── venv/                 # Virtual environment (ignored in Git)
│── db.sqlite3            # SQLite database file
│── manage.py             # Django management script
│── .gitignore            # Files and folders to ignore in Git
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

---

## 🚀 Future Enhancements  
📌 **Task Reminders** – Email reminders for pending tasks.  
📌 **User Authentication** – Allow multiple users to manage tasks separately.  
📌 **Recurring Tasks** – Support for daily, weekly, or monthly tasks.  
📌 **API Support** – RESTful API for integration with mobile apps.  

---

## 🤝 Contributing  
Contributions are welcome! Feel free to fork this repository and submit a pull request.  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 📧 Contact  
📩 **Email:** viveksonkar257@gmail.com  
🔗 **GitHub:** [@vivekso](https://github.com/vivekso)  
