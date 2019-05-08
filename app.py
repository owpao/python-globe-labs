from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/code/<code:code>')
def register(code):
    print("--------code received--------")
    print(code)

if __name__ == '__main__':
    app.run()