'''
Created on Apr 6, 2015

@author: js02sixty
'''
from flask_restful import Resource
from candlemaker.database import init_db, drop_db
from candlemaker.scripts import load_default, load_sample


class InitializeDB(Resource):

    def get(self):
#         try:
        drop_db()
        init_db()
        load_default()
        return {"message": "Database Initialized!"}, 201
#         except:
#             return {"error": "Database Initialization Failed!"}, 500


class InitSampleDB(Resource):

    def get(self):
#         try:
        drop_db()
        init_db()
        load_default()
        load_sample()
        return {"message": "Database initialized with sample data!"}, 201
#         except:
#             return {"error": "Database Initialization Failed!"}, 500
