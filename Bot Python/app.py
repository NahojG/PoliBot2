
import openai
import os
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template
#from config import OPENAI_API_KEY

app = Flask(__name__)
CORS(app)

def leer_clave_api(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read().strip()

ruta_clave_api = '/app/api.txt'
openai.api_key = leer_clave_api(ruta_clave_api)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    input_text = data['question']
    
    # Hacer una solicitud al API de OpenAI usando el modelo gpt-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": input_text}]
    )
    
    # Obtén la respuesta generada
    response_text = response['choices'][0]['message']['content']
    return jsonify(response=response_text)

if __name__ == '__main__':
    app.run(port=5000)

