from flask import request, session, render_template
from server import app, mysql


# Perfiles de usuarios (Si el nick coincide con el de la cookie, activar template edit)
@app.route('/<nick>')
def profile(nick):
    #nick=session['nick']
    return render_template('index.html', nick=nick)