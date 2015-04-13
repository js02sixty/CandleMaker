'''
Created on Apr 6, 2015

@author: js02sixty
'''
from flask import Flask

app = Flask(__name__)
app.config.from_object('candlemaker.default_settings')
app.config.from_envvar('CANDLEMAKER_SETTINGS', silent=True)

# from candlemaker.home import home
from candlemaker.client import client
from candlemaker.apiv1 import apiv1

# app.register_blueprint(home)
app.register_blueprint(client)
app.register_blueprint(apiv1)
