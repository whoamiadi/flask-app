from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/data')
def api_data():
    data = {
        "status": "ok",
        "message": "Flask app is running!",
        "pages": ["home", "about"],
        "version": "1.0"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
