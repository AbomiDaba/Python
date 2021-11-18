from flask_app import app
from flask import render_template, redirect, request
from model.user import User

@app.route('/')
def index():
    return redirect('/user')

@app.route('/user')
def user():
    return render_template('read.html', users = User.get_all())

@app.route('/user/new')
def new():
    return render_template('create.html')

@app.route('/user/create', methods = ['POST'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.save(data)
    return redirect('/user')

@app.route('/user/edit/<int:user_id>')
def edit(user_id):
    data = {
        'id': user_id
    }
    return render_template('edit.html', user = User.get_one(data))

@app.route('/user/update/<int:user_id>', methods = {'POST'})
def update_user(user_id):
    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.update(data)
    return redirect('/user')

@app.route('/user/destroy/<int:user_id>')
def destroy_user(user_id):
    data = {
        'id': user_id
    }
    User.destroy(data)
    return redirect('/user')

@app.route('/user/show/<int:user_id>')
def show_user(user_id):
    data = {
        'id': user_id
    }
    return render_template('show.html', user = User.get_one(data))