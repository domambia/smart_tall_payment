from  config import Config
from flask import Flask 
from mpesa.auth import Auth 

app         = Flask(__name__)
auth        = Auth()
app.config.from_object(Config)



from app import views
