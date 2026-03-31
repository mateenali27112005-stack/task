from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.parser import extract_text
from utils.llm import analyze_cv

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        file = request.files['file']
        jd = request.form.get('jd')

        cv_text = extract_text(file)
        result = analyze_cv(jd, cv_text)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)