from flask_app import app
from flask import render_template, redirect, session, flash, request
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt(app)

app.secret_key = 'iringvneii;ai;jfngri;albjdbd niueeuhrfiuohfr'
@app.route('/')
def index():
    return redirect('/users/register_login')

@app.route('/users/register_login')
def main_page():
    return render_template('main.html')



@app.route('/users/register', methods = ['POST'])
def register():
    print('hi')
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.insert(data)
    session['user_id'] = user_id
    return redirect('/')

@app.route('/users/login', methods = ['POST'])
def login():
    user_in_db = User.get_by_email(request.form)
    if not user_in_db:
        flash('Invalid email or password', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invlid email or password','login')
        return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect('/users/login_page')

@app.route('/users/login_page')
def login_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('login_page.html')

@app.route('/users/logout')
def logout():
    session.pop('user_id')
    return redirect('/')