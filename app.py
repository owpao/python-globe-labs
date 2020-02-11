from flask import Flask, request
import requests

app = Flask(__name__)
app_id = 'koEGIaB7b7u7oc5ARXT7oKudpoRBId6r'
app_secret = '23656f0ac75323df86a38f5880c3a78553ab2704da21207d7c59287c50d7e0a5'

@app.route('/')
def home():
    return 'Hello :)'

# To get the access token, you need to do a POST request via http://developer.globelabs.com.ph/oauth/access_token with your ‘app_id’, 
# ‘app_secret’ and ‘code’ as the parameters. The parameters ‘access_token’ and ‘subscriber_number’ will then be returned to your redirect uri as a response.

@app.route('/access_token', methods=['GET'])
def get_access_token():
    code = request.args.get('code')
    payload = {
        'app_id': app_id,
        'app_secret': app_secret,
        'code': code
    }

    r = requests.post('http://developer.globelabs.com.ph/oauth/access_token', data=payload)
    return r.json()


if __name__ == '__main__':
    app.run(port=8080, debug=True)