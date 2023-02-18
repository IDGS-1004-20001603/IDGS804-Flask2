from flask import Flask, render_template
from flask import request
import forms
from flask_wtf.csrf import CSRFProtect
from collections import Counter
import os

app = Flask(__name__)
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
# csrf = CSRFProtect()

@app.route('/formprueba')
def formprueba():
    return render_template('formprueba.html')

@app.route('/Alumnos', methods=['GET', 'POST'])
def Alumnos():
    reg_alum = forms.UserForm(request.form)
    if(request.method == 'POST'):
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)

    return render_template('Alumnos.html', form = reg_alum)

@app.route('/', methods=['GET', 'POST'])
def Numeros():
    if(request.method == 'POST'):
        numero = int(request.form.get('txtNumeros'))
        return render_template('numeros.html', numero = numero, oculto = '')
    else:
        return render_template('numeros.html', numero = 0, oculto = 'hidden')

@app.route('/valores', methods=['POST'])
def valores():
    if(request.method == 'POST'):
        lista = request.form.getlist('txtNum')
        mayor = max(lista)
        menor = min(lista)
        
        for i in range(len(lista)):
            lista[i] = int(lista[i])
            
        promedio = sum(lista)/len(lista)

        conteo=Counter(lista)
        resultado={}
        for clave in conteo:  
            valor=conteo[clave]
            if valor > 0:
                resultado[clave] = valor

        return render_template('valores.html', lista = lista, mayor = mayor, menor = menor, promedio = promedio, resultados = resultado)

if __name__ == '__main__':
    # csrf.init_app(app)
    app.run(debug=True, port=8080)