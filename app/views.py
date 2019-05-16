from app import app, auth
from flask import request, jsonify
from mpesa.config import Config
import requests
import base64
from datetime import datetime 
from pybase64 import b64encode
from M2Crypto import RSA, X509

config  = Config()



# def password(shortcode, passkey, timestamp):
#     timestamp   = str(timestamp)                                    
#     # data = datetime.strptime(now,'%Y%m%d %H:%M:%S') 
#     timestamp = str(timestamp).replace('-','')
#     timestamp = timestamp.replace(':','') 
#     timestamp  = timestamp.replace(' ', '')
#     timestamp  = timestamp[slice(0,14,1)] 
#     print(timestamp)
#     password  = b64encode(bytes(shortcode + passkey + timestamp, 'utf-8'))
#     data = {'password': password, 'timestamp': timestamp}
#     return data 
# def get_encrypted_password():
#     with open(os.path.join(base_dir, 'cert.cer'), mode = 'r') as f:
#         cert = X509.load_cert_string(f.read()) #reading the file content 
#         #pub_key = X509.load_cert_string(f.read())
#         pub_key = cert.get_pubkey()
#         rsa_key = pub_key.get_rsa()
#         cipher = rsa_key.public_encrypt(bytes('omambia','utf-8'), RSA.pkcs1_padding)
#         return  b64encode(cipher)

@app.route("/")
def home():
    access_token  = auth.get_token()
    print(access_token)
    return "Data is here"

@app.route('/mpesa-validate/', methods = ['GET', 'POST'])
def validate():
    data  = request.get_json()
    response = {
        'ResultCode': 0,
        "ResultDesc": "Successfully validated data"
    }

    print(data)
    return jsonify(response)



@app.route('/mpesa-confirm/', methods = ['GET', 'POST'])
def confirm():
    data  = request.get_json()
    response = {
        'ResultCode': 0,
        "ResultDesc": "Successfully validated data"
    }
    print(data)
    return jsonify(response)



@app.route('/register-url', methods  = ['GET', 'POST'])
def register_url():
    access_token  = auth.get_token()
    api_url = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode": "600388",
        "ResponseType": " ",
        "ConfirmationURL": config.confirmation_url,
        "ValidationURL": config.validate_url}
    response = requests.post(api_url, json = request, headers=headers)
    print (response.text)

    return "Registered Url"

#   "Password": str(),
# "Timestamp": str(password("174379", config.passkey, timestamp)['timestamp']),
@app.route('/stk-push/', methods  = ['GET', 'POST'])
def stk_push():
    access_token  = auth.get_token()
    timestamp = datetime.now()
    timestamp = str(timestamp.strftime("%Y%m%d%H%M%S"))

    password  = '174379'+config.passkey+timestamp
    
    password  = b64encode(bytes(password, 'utf-8'))
    print(password)
    password  = password.decode("utf-8")
    print(password)
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
		  "BusinessShortCode":"174379",
		  "Password": password,
		  "Timestamp": timestamp,
		  "TransactionType": "CustomerPayBillOnline",
		  "Amount": "1",
		  "PartyA": "254721201761", 
		  "PartyB": "174379",
		  "PhoneNumber": "254721201761",
		  "CallBackURL": config.validate_url,
		  "AccountReference": "testpay",
		  "TransactionDesc": " Omambia Buying goods"
		}
    response = requests.post(api_url, json = request, headers=headers)
    print (response.text)

    return "SuccessFully Paid"

