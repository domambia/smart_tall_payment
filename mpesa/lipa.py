import requests 
import  datetime
from .auth import Auth
from mpesa.config import Config
from pybase64 import b64encode


config    = Config()

auth      = Auth()   

class STKPushAPI(object):
    def __init__(self):
        self.headers      = { "Authorization": "Bearer %s" % auth.get_token() }
        self.url          = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        self.timestamp    = datetime.datetime.now()
    def password_and_timestamp(self, shortcode, passkey, timestamp):
        """Processs the current time and generate test password and timestamp"""
        timestamp = str(timestamp.strftime("%Y%m%d%H%M%S"))
        password  = '174379'+config.passkey+timestamp
        password  = b64encode(bytes(password, 'utf-8'))
        password  = password.decode("utf-8")
        data      = {'password': password, 'timestamp': timestamp}
        return data
    def send(self, business_shortcode, amount, phone_number, passkey, callback_url):
        """Processes requests and get the response if successfully."""
        time_passwd =  self.password_and_timestamp(business_shortcode, passkey, self.timestamp)
        req = {
		  "BusinessShortCode": business_shortcode,
		  "Password": time_passwd['password'],
		  "Timestamp": time_passwd['timestamp'],
		  "TransactionType": "CustomerPayBillOnline",
		  "Amount": str(amount),
		  "PartyA": phone_number, 
		  "PartyB": business_shortcode, #shortcode
		  "PhoneNumber": phone_number,
		  "CallBackURL": "http://omambiapayment.tk:5000//stk-response/",
		  "AccountReference": "testpay",
		  "TransactionDesc": " Omambia Buying goods"
		}
        response = requests.post(self.url, json = req, headers=self.headers)
        return response.text 
    
   