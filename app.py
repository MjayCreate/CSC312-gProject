from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "yoursecretkey"

# -----------------------------
# MySQL Configuration
# -----------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'bwave'   
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)


# -----------------------------
# Homepage
# -----------------------------
@app.route('/')
def index():
    return render_template('index.html')


# -----------------------------
# Signup Page
# -----------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Basic validation
        if not username or not password:
            flash("All fields are required!", "danger")
            return redirect('/signup')

        # Hash password
        hashed_password = generate_password_hash(password)

        # Insert into DB
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO tbl_user (username, password) VALUES (%s, %s)",
            (username, hashed_password)
        )
        mysql.connection.commit()
        cur.close()

        flash("Account created successfully!", "success")
        return redirect('/')

    return render_template('signup.html')


# -----------------------------
# Run Application
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
