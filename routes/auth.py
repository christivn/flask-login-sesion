from flask import request, session, render_template, redirect
from server import app, mysql
import requests


# Página principal, renderiza el template del perfil, si está logeado
@app.route('/')
def index():
    try:
        nick=session['nick']
        return render_template('profile.html',nick=nick)
    except:
        return render_template('index.html')



# Página del login
@app.route('/login', methods=['GET'])
def login():
    try:
        nick=session['nick']
        return redirect('/', code=302)
    except:
        return render_template('login.html')



# POST formulario del login
@app.route('/login_form', methods=['POST'])
def login_post():
    try:
        nick=session['nick']
        return render_template('profile.html',nick=nick)
    except:
        try:
            nick_email = request.form['nick-email']
            password = request.form['password']

            url = 'http://127.0.0.1:3000/auth/login'
            obj = {'nick': nick_email, 'password': password}
            r = requests.post(url, data=obj)

            if r.status_code==200:
                session['nick']=nick_email
                return render_template('profile.html',nick=nick)
            else:
                return redirect("/login", code=302)
        except Exception as e:
            print(e)
            return redirect("/login", code=302)



# Logout
@app.route('/logout', methods=['GET'])
def logout():
    try:
        nick=session['nick']
        session.pop('nick', None)
        return redirect("/", code=302)
    except:
        return redirect("/", code=302)