from flask import Flask, render_template, flash
from flask import request, make_response
import forms
from flask_wtf.csrf import CSRFProtect
from collections import Counter
import os
from controllers import resistance, table

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect()


@app.route('/formprueba')
def formprueba():
    return render_template('formprueba.html')


@app.route('/Alumnos', methods=['GET', 'POST'])
def Alumnos():
    reg_alum = forms.UserForm(request.form)
    datos = list()
    if (request.method == 'POST' and reg_alum.validate()):
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)

    return render_template('Alumnos.html', form=reg_alum, datos=datos)


@app.route('/', methods=['GET', 'POST'])
def Numeros():
    if (request.method == 'POST'):
        numero = int(request.form.get('txtNumeros'))
        return render_template('numeros.html', numero=numero, oculto='')
    else:
        return render_template('numeros.html', numero=0, oculto='hidden')


@app.route('/valores', methods=['POST'])
def valores():
    if (request.method == 'POST'):
        lista = request.form.getlist('txtNum')
        mayor = max(lista)
        menor = min(lista)

        for i in range(len(lista)):
            lista[i] = int(lista[i])

        promedio = sum(lista)/len(lista)

        conteo = Counter(lista)
        resultado = {}
        for clave in conteo:
            valor = conteo[clave]
            if valor > 1:
                resultado[clave] = valor

        return render_template('valores.html', lista=lista, mayor=mayor, menor=menor, promedio=promedio, resultados=resultado)


@app.route('/traductor', methods=['GET', 'POST'])
def traductor():
    words = forms.WordsForm(request.form)
    palabraEncontrada = ''
    if (request.method == 'POST'):
        btnGuardar = request.form.get('btnGuardar')
        btnTraducir = request.form.get('btnTraducir')
        if (btnGuardar == 'Guardar' and words.validate()):
            file = open('palabras.txt', 'a')
            file.write('\n' + words.spanish.data.upper() +
                       '\n' + words.english.data.upper())
            file.close()
        if (btnTraducir == 'Traducir'):
            opcion = request.form.get('translate')
            file = open('palabras.txt', 'r')
            palabras = [linea.rstrip('\n') for linea in file]
            if (opcion == 'spanish'):
                spanishWord = request.form.get('txtSpanish')
                for posicion in range(len(palabras)):
                    if (palabras[posicion] == spanishWord.upper()):
                        palabraEncontrada = palabras[posicion - 1]
                        break
                    else:
                        palabraEncontrada = 'No esta en el diccionario'
            elif (opcion == 'english'):
                englishWord = request.form.get('txtSpanish')
                for posicion in range(len(palabras)):
                    if (palabras[posicion] == englishWord.upper()):
                        palabraEncontrada = palabras[posicion + 1]
                        break
                    else:
                        palabraEncontrada = 'No esta en el diccionario'
            file.close()

    return render_template('traductor.html', form=words, palabraEncontrada=palabraEncontrada)


@app.route('/cookie', methods=['GET', 'POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookie.html', form=reg_user))

    if (request.method == 'POST' and reg_user.validate()):
        user = reg_user.username.data
        password = reg_user.password.data
        datos = user + '@' + password
        success_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_usuario', datos)
        flash(success_message)
    return response


@app.route('/resistence', methods=['GET', 'POST'])
def resistence():
    bands = forms.ResistanceForm(request.form)
    boton = request.form.get('btnFormulario')
    ocultar_elemento = 'hidden'
    ocultarTabla = 'hidden'
    band1 = ''
    band2 = ''
    band3 = ''
    band4 = ''
    table_value_resistance = []
    tabla_extra = []
    if (request.method == 'POST'):
        if (boton == 'Calcular'):
            values_resistance = resistance.calculateDataOfResistence(bands)
            table_value_resistance.append(values_resistance)
            ocultar_elemento = ''
            table.writeColors(bands)
        if (boton == 'Mostrar Historial'):
            tabla_extra = table.sendColorsToApp()
            ocultarTabla = 'row'

    return render_template('bandas.html', form=bands, ocultar_elemento=ocultar_elemento, band1=band1,
                           band2=band2, band3=band3, band4=band4, table_value_resistance=table_value_resistance,
                           ocultarTabla=ocultarTabla, tabla_extra=tabla_extra)


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, port=8080)
