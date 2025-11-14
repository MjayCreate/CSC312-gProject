from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(_name_)
app.config['SECRET_KEY'] = 'gTeam_SEN311'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'flask_app_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate form data
        if not username or not password:
            flash('Please fill out all fields with the correct information;', 'error')
            return render_template('signup.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long', 'error')
            return render_template('signup.html')
        
        # Hash the password
        hashed_password = generate_password_hash(password)
        
        # Insert into database
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO tbl_user (username, password) VALUES (%s, %s)",
                (username, hashed_password)
            )
            mysql.connection.commit()
            cur.close()
            
            flash('Registration successful!', 'success')
            return redirect(url_for('home'))
            
        except Exception as e:
            flash('Username already exists or database error', 'error')
    
    return render_template('signup.html')

if _name_ == '_main_':
    app.run(debug=True)