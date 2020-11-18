from . import app
from flask import render_template, request, redirect, session, url_for

app.secret_key = "hello"


@app.route('/')
def index():
    pi=3.141519
    e=2.7
    title = 'Index'
    return render_template('base.html.j2', pi=pi, title=title)


@app.route('/ctverec/',methods=['GET','POST'])
def ctverec():
    title = 'ctverec'
    x = request.args.get('x')
    try:
        z = int(x) * int(x)
        n = int(x) * 4
    except (TypeError, ValueError):
        z = ''
        n = ''
    return render_template('ctverec.html.j2', title=title,z=z,n=n)

@app.route('/kruh/')
def kruh():
    title = 'kruh'
    x = request.args.get('x')
    try:
        z = (int(x)*int(x)) * 3.14
        n = 2 * 3.14 * int(x)
    except (TypeError, ValueError):
        z = ''
        n = ''
    return render_template('kruh.html.j2', title=title,z=z,n=n)    

@app.route('/obdelnik/')
def obdelnik():
    title = 'obdelnik'
    x = request.args.get('x')
    y = request.args.get('y')
    try:
        z = int(x)*int(y)
        n = 2*(int(x)+int(y))
    except (TypeError, ValueError):
        z = ''
        n = ''
    return render_template('obdelnik.html.j2', title=title,z=z,n=n)



@app.route('/tajne/')
def tajne():
    title = 'Tajné'
    return render_template('tajne.html.j2', title=title)



@app.route('/login/',methods=['GET','POST'])
def login():
    title = 'login'
    if request.method == 'POST':
        uzivatel = request.form["nm"]
        session["uzivatel"] = uzivatel
        return redirect(url_for("uzivatel"))
    else:
        return render_template("login.html.j2")
    
    return render_template('login.html.j2', title=title,)

@app.route('/uzivatel')
def uzivatel():
    if "uzivatel" in session:
        uzivatel = session["uzivatel"]
        return redirect(url_for('tajne'))
    else:
        return redirect(url_for("login"))