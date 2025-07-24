from flask import Flask, request, jsonify, render_template

from ollama_prompt import create_noisy_essay


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
    # options = data.get('options', [])  # lista de checkboxes selecionados

    print(f"Texto recebido: {text}")
    print(f"Parâmetros recebidos: {params}")

    res = create_noisy_essay(text, params.get('desvio', ''), 
                             params.get('competencia', ''), params.get('modelo', ''))

    resultado = {
        'message': 'Ruído gerado com sucesso!',
        'input_text': text,
        'used_params': params,
        # 'selected_options': options
    }

    return jsonify(res)