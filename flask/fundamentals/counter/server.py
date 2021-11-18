from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'jnnuuhuhuh216546ihuohuuhgiygiygyi'

@app.route('/')
def sessions():
    if 'count' not in session:
        session['count'] = 0
    session['count']+=1
    return render_template("index.html", count= session['count'])

@app.route('/increment', methods= ['POST'])
def addtwo():
    session['count']+=1
    return redirect('/')

@app.route('/destroy_session', methods= ['POST'])
def clear():
    session.clear()
    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)