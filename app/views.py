from app import app, auth
from flask import request, jsonify, render_template
from mpesa.config import Config
import requests
import base64
from datetime import datetime 
from pybase64 import b64encode
from  app.forms import PayForm

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
    password  = password.decode("utf-8")
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    user_data = request.get_json()
    if user_data:
        phone_number  = user_data['content']['phone_number'] 
        amount        = user_data['content']['amount'] 
        request = {
    		  "BusinessShortCode":"174379", 
              "Password": password, 
              "Timestamp": timestamp, 
              "TransactionType": "CustomerPayBillOnline", 
              "Amount": amount, 
              "PartyA": phone_number, 
    		  "PartyB": "174379",
    		  "PhoneNumber": phone_number,
    		  "CallBackURL": config.validate_url,
    		  "AccountReference": "Smart Toll",
    		  "TransactionDesc": " Please pay for your toll services."
    		}
        response = requests.post(api_url, json = request, headers=headers)
        print (response.text)
        data  = {'status_code': 200, 'content': {'amount_paid': amount}, 'message': 'Success'}
        if response:
            return jsonify(data)
    return render_template("pay.html", form = form)
    


@app.route('/stk-pay/', methods  = ['GET', 'POST'])
def stk_pay():
    access_token  = auth.get_token()
    timestamp = datetime.now()
    timestamp = str(timestamp.strftime("%Y%m%d%H%M%S"))
    password  = '174379'+config.passkey+timestamp
    password  = b64encode(bytes(password, 'utf-8'))
    password  = password.decode("utf-8")
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    form = PayForm()

    if form.validate_on_submit():
        phone_number  = str(form.phone.data) 
        amount        = str(form.amount.data) 
        request = {
    		  "BusinessShortCode":"174379", 
              "Password": password, 
              "Timestamp": timestamp, 
              "TransactionType": "CustomerPayBillOnline", 
              "Amount": amount, 
              "PartyA": phone_number, 
    		  "PartyB": "174379",
    		  "PhoneNumber": phone_number,
    		  "CallBackURL": config.validate_url,
    		  "AccountReference": "Smart Toll",
    		  "TransactionDesc": " Please pay for your toll services."
    		}
        response = requests.post(api_url, json = request, headers=headers)
        print (response.text)
        data  = {'status_code': 200, 'content': {'amount_paid': amount}, 'message': 'Success'}
        if response:
            return jsonify(data)
    return render_template("pay.html", form = form)
    
