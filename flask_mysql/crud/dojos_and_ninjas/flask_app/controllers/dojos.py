from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def main_index():
    return render_template('dojo.html', dojos = dojo.Dojo.get_all())

@app.route('/dojos/create', methods = ['POST'])
def create_dojo():
    dojo.Dojo.insert(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_ninjas(dojo_id):
    data = {
        'id': dojo_id
    }
    return render_template('show.html', dojo = dojo.Dojo.get_one_with_ninjas(data))