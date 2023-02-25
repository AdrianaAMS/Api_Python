
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'Erva Baleeira',
        'nome científico': 'Cordia verbenacea',
        'propriedades medicinais': 'dores articulares, reumatismo,nflamações e fibromialgia'
        
    },
    {
        'id': 2,
        'título': 'Picão preto',
        'nome científico': 'Bidens pilosa',
        'propriedades medicinais': 'hepatite, diurético, diabetes, micoses, e antisséptico'
        
    },
    {
        'id': 3,
        'título': 'Alecrim',
        'nome científico': 'Rosmarinus officinalis L',
        'propriedades medicinais': 'adstringente, tônico, antiflatulento, antiespasmódico, estimulante digestivo, cicatrizante'
        
    },
    {
        'id': 4,
        'título': 'Lavandula angustifolia Mill',
        'nome científico': 'Cordia verbenacea',
        'propriedades medicinais': 'reumatismos, torções e antisséptico'
        
    },

    
]

#Consultar (todos) 
@app.route('/livros',methods=['GET'])
def obter_livros():        #funcao
    return jsonify(livros)


# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        

# Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)



