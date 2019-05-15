from flask import Flask, request
import requests
import logging
import json
import sqlite3
import os

app = Flask(__name__)
app_short_code = '21586712'
app_id = 'koEGIaB7b7u7oc5ARXT7oKudpoRBId6r'
app_secret = '23656f0ac75323df86a38f5880c3a78553ab2704da21207d7c59287c50d7e0a5'

cwd = os.getcwd()
sqlite_file = 'globelabsDB.sqlite'
sqlitedb = '%s\\%s' % (cwd, sqlite_file)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/', methods=['GET'])
def register():
    app.logger.info("--------code received--------")
    code = request.args.get('code')
    app.logger.info("CODE: "+code)

    globelabs_api = 'https://developer.globelabs.com.ph/oauth/access_token'

    data = {'app_id':app_id, 
        'app_secret':app_secret, 
        'code':code} 

    app.logger.info("\ndata: %s",(data))

    response = requests.post(url = globelabs_api, data = data) 
    if(response.status_code == 200):
        
        subscriber = json.loads(response.text)
        app.logger.info("token: %s",subscriber["access_token"])
        app.logger.info("mobile number: %s",subscriber["subscriber_number"])

        # insert_subscriber_to_db(subscriber["subscriber_number"], subscriber["access_token"])

        return 'Registered!'
    else:
        return 'Error in response'

    #post response to developer.globelabs.keme keme
    #receive token and subscriber number

def insert_subscriber_to_db(address, access_token):
    conn = sqlite3.connect(sqlitedb)
    c = conn.cursor()
    app.logger.info("inserting...address:%s and access_token: %s" % (address, access_token))
    c.execute('INSERT INTO SUBSCRIBERS (address, access_token) VALUES (?, ?)', (address, access_token))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)