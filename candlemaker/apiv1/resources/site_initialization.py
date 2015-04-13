'''
Created on Apr 6, 2015

@author: js02sixty
'''
from flask_restful import Resource, abort
from candlemaker.database import init_db, drop_db
from candlemaker.scripts import load_default, load_sample
from candlemaker.apiv1 import auth


class InitializeDB(Resource):
    def get(self):
        drop_db()
        init_db()
        load_default()
        return {"message": "Database Initialized!"}, 201


class InitSampleDB(Resource):
    def get(self):
        drop_db()
        init_db()
        load_default()
        load_sample()
        return {"message": "Database initialized with sample data!"}, 201
