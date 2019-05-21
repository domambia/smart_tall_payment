from datetime import datetime, timezone                                           
now = datetime.now()

date_time  = now.strftime('%Y%m%d%H%m%s')
timestamp  = date_time[slice(0, 14,1)]
print(timestamp)

# {
#   "content": {
#     "amount": "10",
#     "phone_number": '257400000232'
#   }, 
#   "message": "Success", 
#   "status_code": 200
# }

#access_token  = auth.get_token()
#    timestamp = datetime.now()
#    timestamp = str(timestamp.strftime("%Y%m%d%H%M%S"))
#    password  = '174379'+config.passkey+timestamp
#    password  = b64encode(bytes(password, 'utf-8'))
#    password  = password.decode("utf-8")
#    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#    headers = { "Authorization": "Bearer %s" % access_token }
#    user_data = request.get_json()
#    if user_data:
#        phone_number  = user_data['content']['phone_number'] 
#        amount        = user_data['content']['amount'] 
#        req = {
#    		  "BusinessShortCode":"174379", 
#              "Password": password, 
#              "Timestamp": timestamp, 
#              "TransactionType": "CustomerPayBillOnline", 
#              "Amount": amount, 
#              "PartyA": phone_number, 
#    		  "PartyB": "174379",
#    		  "PhoneNumber": phone_number,
#    		  "CallBackURL": config.validate_url,
#    		  "AccountReference": "Smart Toll",
#    		  "TransactionDesc": " Please pay for your toll services."
#    		}
#        response = requests.post(api_url, json = req, headers=headers)
#        print (response.text)
#        # data  = {'status_code': 200, 'content': {'amount_paid': amount}, 'message': 'Success'}
#        if response:
#            return "<p style = margin: auto 30px;> This is a test. Thank you.</p>"
#    return "Payment Is here"