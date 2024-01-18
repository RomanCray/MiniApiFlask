from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def root():
    return "Bienvenido a la mini api de FLASK"
    
@app.route('/usuarios/<nombre>')
def get_user(nombre):
    usuario = {
        "El nuevo usuario es: ": nombre,        
    }

    return jsonify(usuario), 200

@app.route('/usuarios', methods=["POST"])
def create_user():
    data = request.get_json()
    data["mensaje"] = "Usuario creado con exito!"    

    return jsonify(data), 200

if __name__ == "__main__":
    app.run()

    