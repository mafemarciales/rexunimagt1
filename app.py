from flask import Flask, render_template
from flask import request, redirect,url_for
import re 

app =Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/results')
def rs():
    return render_template('resps.html')

@app.route('/resultn')
def rn():
    return render_template('respn.html')

@app.route('/comprobar',methods=['POST'])
def validar():
    if request.method == 'POST':
        cadena=request.form['expresion']
        val=validate(cadena)
        if val:
            return redirect(url_for('rs'))
        else:
            return redirect(url_for('rn'))
    return "no recibido"


def validate(cad):
    lenguaje = re.match('([A-Z])(\d){3}([a-z]){3}(\W){3}',cad) 
    if lenguaje is None:
        return False
    else:
        return True

if __name__ == '__main__' :
    app.run(port=3000,debug=True)
