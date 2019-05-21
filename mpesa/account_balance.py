import requests
from .auth import Auth
from .config import Account



account         = Account()
auth            = Auth()

class AccountBalance(object):
    def __init__(self):
        self.headers  = {"Authorization": "Bearer %s" % auth.get_token()}
    
    def send(self, initiator, party_A, identifier_type, result_url, queue_url, remarks):
        req = { "Initiator": initiator,
                  "SecurityCredential": auth.get_password(),
                  "CommandID":"AccountBalance",
                  "PartyA":party_A,
                  "IdentifierType":"4",
                  "Remarks": remarks,
                  "QueueTimeOutURL": queue_url,
                  "ResultURL": result_url
                 }
        response = requests.post(account.url, json = req, headers=self.headers)
        data =  response.text
        print(data)
        return data
    
    
    