from flask import Flask, request, jsonify
from CaixaEletronico import CaixaEletronico

app = Flask(__name__)
caixa_eletronico = CaixaEletronico()

@app.route('/api/saque', methods=['POST'])
def saque():
    dados = request.get_json()

    if 'valor' not in dados:
        return jsonify({"erro": "O campo 'valor' é obrigatório."}), 400

    try:
        valor = int(dados['valor'])
        resultado = caixa_eletronico.calcular_cedulas(valor)
        return jsonify(resultado)
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
