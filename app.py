from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/seguranca')
def seguranca():
    return render_template('seguranca.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

if __name__ == '__main__':
    app.run(debug=True)
