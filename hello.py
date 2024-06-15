from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world! bassshar'

@app.route('/contact')
def contact():
    return 'A7la mesa on you from Abushaymaa :)'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
