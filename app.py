import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        prompt = request.json['prompt']
        model = genai.GenerativeModel('imagen-3.0-generate-002')
        response = model.generate_content(prompt)
        image_data = response.candidates[0].content.parts[0].inline_data.data
        return jsonify({'image_data': image_data})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
