import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
import base64

app = Flask(__name__)

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API Key not found. Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        prompt = request.json['prompt']
        model = genai.GenerativeModel('gemini-2.5-flash-image-preview')
        response = model.generate_content(prompt)

        image_data_bytes = response.candidates[0].content.parts[0].inline_data.data
        image_data_base64 = base64.b64encode(image_data_bytes).decode('utf-8')

        return jsonify({'image_data': image_data_base64})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500