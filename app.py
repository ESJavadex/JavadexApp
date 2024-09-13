import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensajes', methods=['GET'])
def mensajes():
    ref = db.reference('mensajes')
    mensajes = ref.get()
    return jsonify(mensajes), 200

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # Debug print
        mensaje = data.get('mensaje')
        if mensaje:
            ref = db.reference('mensajes')
            nuevo_mensaje = ref.push({
                'mensaje': mensaje
            })
            print(f"Mensaje saved with ID: {nuevo_mensaje.key}")  # Debug print
            return jsonify({'status': 'Mensaje enviado', 'id': nuevo_mensaje.key}), 200
        else:
            print("No message provided")  # Debug print
            return jsonify({'error': 'No se proporcionó ningún mensaje'}), 400
    except Exception as e:
        print(f"An error occurred: {e}")  # Print detailed error
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

