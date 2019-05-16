import requests 
import json
from mpesa.config import Config
from requests.auth import HTTPBasicAuth
config  = Config()

class Auth(object):

    def get_token(self):
        request  = requests.get(config.auth_url, 
                                auth  = HTTPBasicAuth(
                                    config.consumer_key, 
                                    config.consumer_secret))
        data = json.loads(request.text)
        return data['access_token']

        
