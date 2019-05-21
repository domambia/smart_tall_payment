import requests 
import json
import os
from mpesa.config import Config, Account
from requests.auth import HTTPBasicAuth
#from M2Crypto import RSA, X509
from pybase64 import b64encode




config      = Config()
account     = Account() 
base_dir    = os.path.dirname(os.path.realpath(__file__))

account 
class Auth(object):

    def get_token(self):
        request  = requests.get(config.auth_url, 
                                auth  = HTTPBasicAuth(
                                    config.consumer_key, 
                                    config.consumer_secret))
        data = json.loads(request.text)
        return data['access_token']
    
    
    def get_password(self):
        pass
#        with open(os.path.join(base_dir, 'cert.cer'), mode = 'r') as f:
#            cert = X509.load_cert_string(f.read()) #reading the file content 
#            pub_key = cert.get_pubkey()
#            rsa_key = pub_key.get_rsa()
#            cipher = rsa_key.public_encrypt(bytes(account.security_credential,'utf-8'), RSA.pkcs1_padding)
#            return  b64encode(cipher).decode("utf-8")
    
#aut  = Auth()
#print(aut.get_password())
#
#
#        
