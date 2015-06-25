'''
Created on Apr 6, 2015

@author: js02sixty
'''

## Flask
DEBUG = True
SECRET_KEY = '5xmYet-6^92JEJEm'

## DB
DATABASE_SETTINGS = 'postgresql+psycopg2://candlemaker:Security#321@127.0.0.1:5432/candlemaker'

## JWT Authentication
JWT_AUTH_URL_RULE = '/api/v1/auth'
JWT_EXPIRATION_DELTA = 1800  # 5 hours
