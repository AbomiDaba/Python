from logging import fatal
from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.survey import Survey


app.secret_key = 'jflkajljfioefuirf564656465465465f4654g655g56r4g54'

@app.route('/')
def  index():
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def survey():
    if not Survey.validate_survey(request.form):
        return redirect('/')
    Survey.create(request.form)
    return redirect('/result')

@app.route('/result')
def results():
    return render_template("result.html",survey = Survey.get_last())