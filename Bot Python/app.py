
import openai
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template
from config import OPENAI_API_KEY

app = Flask(__name__)
CORS(app)

openai.api_key = OPENAI_API_KEY

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

