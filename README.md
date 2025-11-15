
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


# 🚀 **Quick Start — Clone and Run**

1️⃣ **Clone the repository**

```bash
git clone https://github.com/MjayCreate/CSC312-gProject/tree/bright
cd CSC312-gProject
```

> Optional: You can also download the ZIP from GitHub and extract it.

---

2️⃣ **Make sure Python and MySQL are installed**

* Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* MySQL Server + Workbench: [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/)

Git Bash is optional but recommended.

---

3️⃣ **Run the app**

Open Git Bash or Command Prompt in the project folder:

```bash
python app.py
```

---

4️⃣ **Open your browser**

Go to:

```
http://127.0.0.1:5000
```

Your homepage and signup page will load automatically.

---

✅ **Done!** No extra setup needed — everything is ready to run.



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

```

