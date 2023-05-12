import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

# Модель User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Авторизация пользователя
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # Вход выполнен успешно
            return redirect('/users')
        else:
            # Неверные учетные данные
            return render_template('login.html', error=True)
    else:
        return render_template('login.html', error=False)

# Создание пользователя
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect('/users')
    else:
        return render_template('register.html')

# Список пользователей
@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

# Редактирование пользователя
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = User.query.get(user_id)
    
    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']
        db.session.commit()
        
        return redirect('/users')
    else:
        return render_template('edit.html', user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
