from flask import Flask, request, redirect
from util.globelabs3 import Globe
import logging
import json
import sqlite3

app = Flask(__name__)
app_short_code = '21586712'
app_id = 'koEGIaB7b7u7oc5ARXT7oKudpoRBId6r'
app_secret = '23656f0ac75323df86a38f5880c3a78553ab2704da21207d7c59287c50d7e0a5'
globe = Globe(app_id=app_id, app_secret=app_secret, shortcode=app_short_code)

@app.route('/')
def register():
    r = globe.get_access_token(request.args.get('code'))
    response = json.loads(r.text)
    print("accessTOKEN: "+response.get('access_token'))
    ac = response.get('access_token')
    subscriber_number = response['subscriber_number']
    print("access token: "+ac)
    print("subscriber number: "+subscriber_number)
    return "Success! You are now registered! :)"


if __name__ == '__main__':
    app.run(debug=True)