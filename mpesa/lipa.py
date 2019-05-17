import requests 
import  datetime

class STKPushAPI(object):
    """
    Module that process the Mpesa STK-Push Operations.
    Data Members: 
        headers  --> Defines the headers and token for the push.
        url      --> this gives the stk-push url, get it from mpesa incase if it has changed.
        timestamp -->  the time of making the request. This is used to generate the password and the passkey too.
    """
	def __init__(self):
		self.headers      = { "Authorization": "Bearer %s" % auth.get_token() }
		self.url          = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
		self.timestamp    = datetime.datetime.now()

	def password_and_timestamp(shortcode, passkey, timestamp):
        """
        Processs the current time and generate test password and timestamp"""
        
		timestamp = str(timestamp.strftime("%Y%m%d%H%M%S"))
        password  = '174379'+config.passkey+timestamp
        password  = b64encode(bytes(password, 'utf-8'))
        password  = password.decode("utf-8")
        data      = {'password': passwod, 'timestamp': timestamp}
        return data
    
    def send(self, business_shortcode, 
             amount, party_a, party_b, phone_number, callback_url,  transaction_desc):
        """
        Processes requests and get the response if successfully."""
        time_passwd =  password_and_timestamp(shortcode, passkey, timestamp)
        req = {
		  "BusinessShortCode": business_shortcode,
		  "Password": time_passwd['password'],
		  "Timestamp": time_passwd['timestamp'],
		  "TransactionType": "CustomerPayBillOnline",
		  "Amount": amount,
		  "PartyA": phone_number, 
		  "PartyB": business_shortcode, #shortcode
		  "PhoneNumber": phone_number,
		  "CallBackURL": callback_url,
		  "AccountReference": "testpay",
		  "TransactionDesc": " Omambia Buying goods"
		}
        response = requests.post(api_url, json = req, headers=headers)
        return response.text 

