'''
Created on Apr 6, 2015

@author: js02sixty
'''

from flask import Blueprint
from flask_restful import Api, abort
from flask_httpauth import HTTPDigestAuth
from candlemaker.models import User
from flask_restful import Resource, reqparse

auth = HTTPDigestAuth()

@auth.get_password
def get_pw(username):
    users = User.query.filter(User.username == username).one()  # @UndefinedVariable
    if username == users.username:
        return users.password
    return None

def group_check(user, group):
    u = User.query.filter(User.username == user).first()  # @UndefinedVariable
    if group in u.group.name:
        return True

    
errors = {
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


apiv1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
api = Api(apiv1, errors=errors)


class Info(Resource):
    
    @auth.login_required
    def get(self):
        return {'message': 'hello ' + auth.username()}

from candlemaker.apiv1.resources.users import UserListApi, UserApi
from candlemaker.apiv1.resources.user_groups import UserGroupListApi, UserGroupApi
from candlemaker.apiv1.resources.products import (
    ProductListApi,
    ProductApi,
    ProductNoteListApi,
    ProductNoteApi
)
#from resources.notes import NoteApi
from candlemaker.apiv1.resources.site_initialization import (
    InitializeDB, InitSampleDB)

api.add_resource(Info, '/')
api.add_resource(InitializeDB, '/initdb')
api.add_resource(InitSampleDB, '/initsampledb')
api.add_resource(UserListApi, '/users')
api.add_resource(UserApi, '/users/<int:user_id>')
api.add_resource(UserGroupListApi, '/usergroups')
api.add_resource(UserGroupApi, '/usergroups/<int:user_group_id>')
api.add_resource(ProductListApi, '/products')
api.add_resource(ProductApi, '/products/<int:product_id>')
api.add_resource(ProductNoteListApi, '/products/<int:product_id>/notes')
api.add_resource(ProductNoteApi, '/products/<int:product_id>/notes/<int:note_id>')
