import requests

shortcode = '21586712'
access_token ='YclQQ99LQGooG5yRcs7Y-Ms88vKLchWM8hVMl1el3MU'
app_uri = 'https://devapi.globelabs.com.ph/smsmessaging/v1/outbound/6712/requests?access_token=YclQQ99LQGooG5yRcs7Y-Ms88vKLchWM8hVMl1el3MU'

payload_data = {
    "clientCorrelator":"12345",
    "senderAddress": "6712",
    "message":"hello pao",
    "address":"09154996738"
}

print("\ndata: %s" % (payload_data))
# app.logger.info("\ndata: %s",(payload_data))

response = requests.post(url = app_uri, data = payload_data) 
print(response.status_code)
if(response.status_code == 200 or response.status_code ==201):
    print("Message Sent!")