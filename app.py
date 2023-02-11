from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/formprueba')
def formprueba():
    return render_template('formprueba.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)