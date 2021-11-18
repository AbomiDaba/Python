from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja


@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/ninjas/create', methods = ['POST'])
def new_ninjas():
    ninja.Ninja.insert(request.form)
    return redirect('/dojos')

@app.route('/ninja/destroy/<int:ninja_id>/<int:dojo_id>')
def destroy_ninja(ninja_id, dojo_id):
    data = {
        'id': ninja_id
    }
    ninja.Ninja.destroy(data)
    return redirect(f'/dojos/{dojo_id}')