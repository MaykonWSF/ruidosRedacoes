from flask import Flask, request, jsonify, render_template


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

    # Exemplo de processamento: montar um resultado simples
    # Aqui você implementaria seu gerador de ruídos usando `text` e `params`
    resultado = {
        'message': 'Ruído gerado com sucesso!',
        'input_text': text,
        'used_params': params
    }

    return jsonify(resultado)