
from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask_cors import CORS

app = Flask(__name__, static_folder='/Users/nahojgranados/Downloads/static', template_folder='/Users/nahojgranados/Downloads/templates')
CORS(app)

# Load your model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-125M')
model = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-125M')

@app.route('/')
def home():
    return render_template('chat.html')  # Ensure your HTML file is named chat.html

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    input_text = data['question']
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=200)
    response_text = str(tokenizer.decode(output[0], skip_special_tokens=True))
    return jsonify(response=response_text)

if __name__ == '__main__':
    app.run(port=5000)  # Listen on TCP port 5000
