from flask import Flask, render_template
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administracao_redes_locais')
def administracao_redes_locais():
    return render_template('administracao_redes_locais.html')

@app.route('/processamento_computacional')
def processamento_computacional():
    return render_template('Processamento computacional/processamento_computacional.html')

@app.route('/descricao_funcionamento')
def descricao_funcionamento():
    return render_template('Processamento computacional/descricao_funcionamento.html')


@app.route('/c_e_cplusplus')
def c_e_cplusplus():
    return render_template('c_e_cplusplus.html')

@app.route('/administracao_de_bd')
def administracao_de_bd():
    return render_template('administracao_de_bd.html')

@app.route('/prog_com_java')
def prog_com_java():
    return render_template('prog_com_java.html')

@app.route('/prog_com_py')
def prog_com_py():
    return render_template('prog_com_py.html')


if __name__ == '__main__':
    app.run(debug=True)
else:
    app = app  # Isso garante que o Vercel encontre o aplicativo Flask