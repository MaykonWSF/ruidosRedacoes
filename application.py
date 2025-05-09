from flask import Flask, request, jsonify, render_template

from competencia1 import Competencia1


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Rota para receber dados do front-end
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Nenhum dado recebido'}), 400

    text = data.get('text', '')
    params = data.get('params', {})  # dicionário {'param1': '50', ...}
    options = data.get('options', [])  # lista de checkboxes selecionados

    if 'param1' in params:
        c1 = Competencia1(text, int(params.get('param1')))
        c1.adicionar_ruido()

    resultado = {
        'message': 'Ruído gerado com sucesso!',
        'input_text': text,
        'used_params': params,
        'selected_options': options
    }

    return jsonify(resultado)