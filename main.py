import sqlite3, random

from flask import Flask, render_template, request, redirect, url_for, flash, g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = '''b'7A\xec\xb6\x83A\x0c\xacH\x9a\x18\xc3\xd0\xf1\x07\xd2\xfa\xd7t\x80\xdf\x0f3\xea'
'''

DATABASE = 'database.db'

balance = 1000

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.before_request
def before_request():
    get_db()


@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/game')
def random_game():
    symbols = ['-100$', '-1000$', '-10000$', '-100000$', '-500000$', '+100$', '+500$', '+10000$']  # Символи крутилки
    result = [random.choice(symbols) for _ in range(1)]
    return render_template("game.html", result=result)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')  # Використання імені для аутентифікації
        password = request.form.get('password')

        db = get_db()  # Підключення до бази даних
        cursor = db.execute("SELECT * FROM users WHERE name = ?", (name,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):  # Перевірка пароля
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Перехід на домашню сторінку
        else:
            flash('Invalid name or password', 'error')

    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        repl_password = request.form.get('repl_password')

        # Перевірка заповнення полів і збігу паролів
        if not all([name, email, password, repl_password]):
            flash('Please fill in all the fields', 'error')
        elif password != repl_password:
            flash('Passwords do not match', 'error')
        else:
            try:
                db = get_db()
                # Перевірка на наявність користувача з таким же email
                cursor = db.execute("SELECT id FROM users WHERE email = ?", (email,))
                if cursor.fetchone():
                    flash('Email is already registered', 'error')
                else:
                    # Хешування пароля
                    hashed_password = generate_password_hash(password, method='scrypt')
                    # Вставка даних в базу
                    db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                               (name, email, hashed_password))
                    db.commit()
                    flash('Registration successful', 'success')
                    return redirect(url_for('home'))
            except sqlite3.Error as e:
                flash(f"An error occurred: {e}", 'error')
                print(f"Name: {name}, Email: {email}, Password: {password}")

    return render_template('register.html')




if __name__ == "__main__":
    app.run(port=7777, debug=True)