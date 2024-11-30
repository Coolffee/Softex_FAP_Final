
# tem que instalar o flask, lembrando
from flask import Flask, request, jsonify, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Usuários para autenticação básica (depois ver sobre o JWT)
USERS = {
    "admin": generate_password_hash("admin")
}


@auth.verify_password
def authenticate(username, password):
    """Autenticação básica simples para demonstração."""
    if username in USERS and check_password_hash(USERS[username], password):
        return username
    return None


PRODUCTS = [
    {'id': 1, 'name': 'Product A', 'price': 10.99, 'stock': 100},
    {'id': 2, 'name': 'Product B', 'price': 25.50, 'stock': 50}
]

NEXT_PRODUCT_ID = 3


#Função auxiliar para buscar um produto pelo ID
def find_product(product_id):
    """Busca um produto na lista pelo ID, retorna None se não encontrar"""
    for product in PRODUCTS:
        if product['id'] == product_id:
            return product
    return None


@app.route('/products', methods=['GET'])
@auth.login_required
def get_products():
    """Retorna a lista de produtos."""
    return jsonify(PRODUCTS)


@app.route('/products/<int:product_id>', methods=['GET'])
@auth.login_required
def get_product(product_id):
    """Retorna um produto específico pelo ID."""
    product = find_product(product_id)
    if product:
        return jsonify(product)
    else:
        abort(404, description=f"Produto com ID {product_id} não encontrado.")


@app.route('/products', methods=['POST'])
@auth.login_required
def create_product():
    """Cria um novo produto."""
    global NEXT_PRODUCT_ID
    data = request.get_json()

    #Validação básica dos dados
    if not data or 'name' not in data or 'price' not in data or 'stock' not in data:
        abort(400, description="Dados inválidos.  São necessários 'name', 'price' e 'stock'.")

    try:
        new_product = {
            'id': NEXT_PRODUCT_ID,
            'name': data['name'],
            'price': float(data['price']),
            'stock': int(data['stock'])
        }
        PRODUCTS.append(new_product)
        NEXT_PRODUCT_ID += 1
        return jsonify(new_product), 201
    except ValueError:
        abort(400, description="Preço e estoque devem ser números.")


@app.route('/products/<int:product_id>', methods=['PUT'])
@auth.login_required
def update_product(product_id):
    """Atualiza um produto existente."""
    product = find_product(product_id)
    if not product:
        abort(404, description=f"Produto com ID {product_id} não encontrado.")
    data = request.get_json()
    if not data:
        abort(400, description="Dados inválidos.")

    try:
        #Atualiza apenas os campos fornecidos na requisição
        for key, value in data.items():
            if key in ['name', 'price', 'stock']:
                if key == 'price':
                    value = float(value)
                elif key == 'stock':
                    value = int(value)
                product[key] = value
        return jsonify(product)
    except ValueError:
        abort(400, description="Preço e estoque devem ser números.")


@app.route('/products/<int:product_id>', methods=['DELETE'])
@auth.login_required
def delete_product(product_id):
    """Deleta um produto."""
    product = find_product(product_id)
    if not product:
        abort(404, description=f"Produto com ID {product_id} não encontrado.")
    PRODUCTS.remove(product)
    return jsonify({'message': 'Produto deletado'}), 204


if __name__ == '__main__':
    app.run(debug=True)