'''
Created on Apr 6, 2015

@author: js02sixty
'''
from flask import Flask
from flask_restful import Api, abort, wraps
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required, current_user
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
import json

ERRORS = {
    'IntegrityError': {
        'message': 'Record already exists!',
        'status': 409
    },
    'AttributeError': {
        'message': 'Record not found!',
        'status': 404
    },
    'NoResultFound': {
        'message': 'Not Found',
        'status': 404
    }
}

app = Flask(__name__)
app.config.from_object('candlemaker.default_settings')
app.config.from_envvar('CANDLEMAKER_SETTINGS', silent=True)
jwt = JWT(app)
api = Api(app, prefix='/api/v1', errors=ERRORS)


from candlemaker.database import db_session
from candlemaker.models import User
# from candlemaker.home import home
from candlemaker.client import client


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@jwt.authentication_handler
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    return user


@jwt.user_handler
def load_user(payload):
    user = User.query.filter(User.id == payload['id']).first()
    if not user:
        return False
    return user


@jwt.payload_handler
def make_payload(user):
    return {
        'id': user.id,
        # 'exp': datetime.utcnow() + app.config['JWT_EXPIRATION_DELTA']
        'username': user.username
    }


class Info(Resource):
    @jwt_required()
    def get(self):
        return {'message': 'Hello ' + current_user.username}


from resources.users import UserListApi, UserApi
from resources.user_groups import UserGroupListApi, UserGroupApi
from resources.products import (
    ProductListApi,
    ProductApi,
    ProductNoteListApi,
    ProductNoteApi
)
from resources.notes import NoteApi
from resources.site_initialization import (
    InitializeDB, InitSampleDB)

api.add_resource(Info, '/info')
api.add_resource(InitializeDB, '/initdb')
api.add_resource(InitSampleDB, '/initsampledb')
api.add_resource(UserListApi, '/users')
api.add_resource(UserApi, '/users/<int:user_id>')
api.add_resource(UserGroupListApi, '/usergroups')
api.add_resource(UserGroupApi, '/usergroups/<int:user_group_id>')
api.add_resource(ProductListApi, '/products')
api.add_resource(ProductApi, '/products/<int:product_id>')
api.add_resource(ProductNoteListApi, '/products/<int:product_id>/notes')
api.add_resource(
    ProductNoteApi, '/products/<int:product_id>/notes/<int:note_id>')

# app.register_blueprint(home)
app.register_blueprint(client)
