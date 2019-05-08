from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register')
def register(code):
    print(code)

if __name__ == '__main__':
    app.run()