from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from chatbot import top_keywords, query_engine

app = Flask(__name__)
CORS(app)

keyword_response = str(query_engine.query("Tell me top 4 one word keywords"))
keywords = top_keywords(keyword_response)

@app.route('/')
def index():
    return redirect(url_for('chat'))

@app.route('/chat')
def chat():
    return render_template('chat.html', keywords=keywords)

@app.route('/health')
def health():
    return 'ok'

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()

        if not data or 'question' not in data:
            return jsonify({'status': False, 'response': 'Question not provided'})

        ques = data['question']

        response = query_engine.query(ques)

        return jsonify({'status': True, 'response': str(response)})
    except Exception as e:
        return jsonify({'status': False, 'response': str(e)})

if __name__ == '__main__':
    app.run(debug=True)