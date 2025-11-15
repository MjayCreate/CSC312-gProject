
# Flask Signup App (with MySQL Database)

This is a simple Flask web application that teaches beginners how a real web app works.  
It contains:

- A homepage  
- A signup page  
- A MySQL database for storing users  
- Secure password hashing  
- Bootstrap for simple styling  

This project is part of our group lab CSC312

---

## 📂 Project Structure

```

flask-signup-app/
│ app.py
│ requirements.txt
│ README.md
├── templates/
│   ├── index.html
│   └── signup.html
└── sql/
└── create_db.sql

````

---

# 🚀 HOW TO SET UP AND RUN THE PROJECT (WINDOWS — GIT BASH)

Follow these steps **exactly**.

---

## 1️⃣ Install Python

Download Python from:  
https://www.python.org/downloads/

During installation ✔ **check “Add Python to PATH”**

---

## 2️⃣ Open Git Bash

Right-click inside your project folder → **Git Bash Here**

---

## 3️⃣ Create a Virtual Environment

```bash
python -m venv 
````

Activate it:

```bash
source venv/Scripts/activate
```

If successful, your terminal will show:

```
(venv)
```

---

## 4️⃣ Install Project Requirements

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Set Up MySQL Database

You must have **MySQL Server** + **MySQL Workbench** installed.

### Create the database:

1. Open **MySQL Workbench**
2. Run the script inside `sql/create_db.sql`

```sql
CREATE DATABASE IF NOT EXISTS flaskdb;
USE flaskdb;

CREATE TABLE tbl_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

---

## 6️⃣ Create Your `.env` File

Inside the project folder, create a file named **.env**

Copy this inside it:

```
SECRET_KEY=mysupersecretkey
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=YOUR_MYSQL_PASSWORD
MYSQL_DB=flaskdb
```

Replace:

* `YOUR_MYSQL_PASSWORD` → with your real MySQL password

---

## 7️⃣ Run the Application

Inside Git Bash (with virtual env activated):

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

You can now use the homepage and the signup page!

---

# 📄 Explanation of Each File

### **1. app.py**

This is the main Python file that runs the entire application.

It contains:

* Flask app setup
* Database connection
* Homepage route (`/`)
* Signup route (`/signup`)
* Password hashing before saving users

### **2. templates/index.html**

This is the homepage.
It uses simple Bootstrap for styling.

### **3. templates/signup.html**

This contains the signup form where the user enters:

* username
* password

It sends the form to the backend using POST.

### **4. sql/create_db.sql**

This file contains the SQL script to create the database and user table.

### **5. requirements.txt**

This file lists all the Python packages needed for the project.
Installing them is done using:

```bash
pip install -r requirements.txt
```

### **6. .env**

Stores your secret settings such as:

* database username
* database password
* app secret key

You must *not* upload `.env` to GitHub.

---

# 🔐 Password Security (Beginner Explanation)

When users sign up, we **never** store their real password.

Instead, Flask converts the password into something unreadable called a **hash**.

Even if someone sees the database, they **cannot** read the real passwords.

This is handled using:

```python
from werkzeug.security import generate_password_hash
```

---

# 🎯 What You Learn From This Project

By doing this project, you will understand:

* How Flask apps are structured
* How to create routes (pages)
* How to use templates (HTML files)
* How to work with forms and request data
* How to connect Python to a MySQL database
* How to hash passwords (security basics)
* How to use virtual environments
* How to install and manage dependencies

This covers the foundation of backend development with Flask.

---

# 📘 Next Learning Steps (Optional Improvements)

Students can extend this project by:

* Adding login functionality
* Creating a dashboard page
* Validating form inputs properly
* Showing a list of all users
* Adding CSS styling
* Adding logout functionality
* Adding flash messages (already included in example)

---

# 🙌 Final Notes

This README is intentionally simple so beginners can follow it without confusion.

Happy coding! 🎉

```

