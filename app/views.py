from app import app, auth
from flask import request, jsonify, render_template
from mpesa.config import Config
import requests
import base64
from datetime import datetime 
from pybase64 import b64encode
from  app.forms import PayForm
from mpesa.lipa import STKPushAPI
from mpesa.account_balance import AccountBalance
from mpesa.config import Account

account                 = Account()
account_balance         = AccountBalance()
config                  = Config()
stk                     = STKPushAPI()


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



'''
Handle the STK Push Response
'''
@app.route('/stk-response/', methods = ['GET', 'POST'])
def stk_response():
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
    req = { "ShortCode": "600388",
        "ResponseType": " ",
        "ConfirmationURL": config.confirmation_url,
        "ValidationURL": config.validate_url}
    response = requests.post(api_url, json = req, headers=headers)
    print (response.text)

    return "Registered Url"

#   "Password": str(),
# "Timestamp": str(password("174379", config.passkey, timestamp)['timestamp']),
@app.route('/stk-push/', methods  = ['GET', 'POST'])
def stk_push():
    user_data = request.get_json()
    if user_data:
        phone_number  = user_data['content']['phone_number'] 
        amount        = user_data['content']['amount'] 
        req  = stk.send(config.mpesa_bs_shortcode, amount, phone_number, config.passkey, config.validate_url)
        if req:
            resp = {"status_code": 200, "content": {'paid': "success"}, "message": "Success"}
            return jsonify(resp)
        resp = {"status_code": 404, "content": {'paid': "unsuccess"}, "message": "Unsuccess"}
        return jsonify(resp)
    
    

@app.route('/stk-pay/', methods  = ['GET', 'POST'])
def stk_pay():
    form    = PayForm()
    if form.validate_on_submit():
        phone_number    = form.phone.data
        amount          = form.amount.data
        req  = stk.send(config.mpesa_bs_shortcode, amount, phone_number, config.passkey, config.validate_url)
        if req:
            resp = {"status_code": 200, "content": {'paid': "success"}, "message": "Success"}
            return jsonify(resp)
        resp = {"status_code": 404, "content": {'paid': "unsuccess"}, "message": "unsuccess"}
        return jsonify(resp)
    return render_template("pay.html", form = form)
    
    
@app.route('/best-way', methods  = ['GET', 'POST'])
def best_way():
    form    = PayForm()
    if form.validate_on_submit():
        phone_number    = form.phone.data
        amount          = form.amount.data
        req  = stk.send(config.mpesa_bs_shortcode, amount, phone_number, config.passkey, config.validate_url)
        if req:
            return "Success"
        return "Failed"
    return render_template("pay.html", form = form)



@app.route('/account-balance',  methods = ['GET', 'POST'])
def account_bal():
    remarks  = "Welcome Home is good for payment to your loved coders"
    req  = account_balance.send(account.initiator, account.party_A, 
             account.identifier_type, account.result_url, account.queue_time_out_URL, remarks)
    
    if req:
        resp = {"status_code": 200, "content": {'paid': "success"}, "message": "Success"}
        return jsonify(resp)
    resp = {"status_code": 200, "content": {'paid': "success"}, "message": "Success"}
    return "Applications Omambia"
