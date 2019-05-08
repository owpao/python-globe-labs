from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<code>')
def register(code):
    print("--------code received--------")
    print("CODE: "code)

    #post response to developer.globelabs.keme keme
    #receive token and subscriber number

if __name__ == '__main__':
    app.run()