# professional_flask_ui.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from utils import get_welcome_message, process_contact_form
from datetime import datetime
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey123'  # Secure secret key for sessions and flash messages

# Database initialization
def init_db():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS contact_submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        # Insert sample portfolio data if empty
        c.execute('SELECT COUNT(*) FROM portfolio')
        if c.fetchone()[0] == 0:
            sample_projects = [
                ('AI Dashboard', 'A responsive dashboard for AI analytics.', '/static/images/project1.jpg'),
                ('E-Commerce Platform', 'A full-stack e-commerce solution.', '/static/images/project2.jpg'),
                ('Portfolio Site', 'A modern portfolio for professionals.', '/static/images/project3.jpg')
            ]
            c.executemany('INSERT INTO portfolio (title, description, image_url) VALUES (?, ?, ?)', sample_projects)
        conn.commit()

# Initialize database on startup
init_db()

# Helper function to validate email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

@app.route('/')
def home():
    message = get_welcome_message()
    return render_template('index.html', welcome_message=message, year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html', year=datetime.now().year)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Please fill in all fields.', 'error')
        elif not is_valid_email(email):
            flash('Please enter a valid email address.', 'error')
        elif len(name) < 3:
            flash('Name must be at least 3 characters long.', 'error')
        elif len(message) < 10:
            flash('Message must be at least 10 characters long.', 'error')
        else:
            success = process_contact_form(name, email, message)
            if success:
                # Save to database
                with sqlite3.connect('database.db') as conn:
                    c = conn.cursor()
                    c.execute('INSERT INTO contact_submissions (name, email, message) VALUES (?, ?, ?)',
 
                    (name, email, message))
                    conn.commit()
                flash('Message sent successfully!', 'success')
                return redirect(url_for('contact'))
            else:
                flash('Failed to send message. Please try again.', 'error')
    
    return render_template('contact.html', year=datetime.now().year)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('SELECT password FROM users WHERE username = ?', (username,))
            result = c.fetchone()
            if result and check_password_hash(result[0], password):
                session['username'] = username
                flash('Logged in successfully!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password.', 'error')
    
    return render_template('login.html', year=datetime.now().year)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if not username or not password or not email:
            flash('Please fill in all fields.', 'error')
        elif not is_valid_email(email):
            flash('Please enter a valid email address.', 'error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
        else:
            try:
                with sqlite3.connect('database.db') as conn:
                    c = conn.cursor()
                    hashed_password = generate_password_hash(password)
                    c.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                            (username, hashed_password, email))
                    conn.commit()
                    flash('Registration successful! Please log in.', 'success')
                    return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Username or email already exists.', 'error')
    
    return render_template('login.html', year=datetime.now().year, register=True)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))
    
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('SELECT name, email, message, submitted_at FROM contact_submissions ORDER BY submitted_at DESC')
        submissions = c.fetchall()
    
    return render_template('dashboard.html', submissions=submissions, year=datetime.now().year)

@app.route('/portfolio')
def portfolio():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('SELECT title, description, image_url, created_at FROM portfolio')
        projects = c.fetchall()
    
    return render_template('portfolio.html', projects=projects, year=datetime.now().year)

@app.route('/api/info')
def api_info():
    return jsonify({
        'app': 'Kamran Flask UI Project',
        'version': '2.0',
        'author': 'Kamran Ali',
        'status': 'Production-ready',
        'features': ['Authentication', 'Portfolio', 'Contact Form', 'Dashboard', 'Responsive Design']
    })

if __name__ == '__main__':
    app.run(debug=True)