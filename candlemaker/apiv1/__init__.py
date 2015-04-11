'''
Created on Apr 6, 2015

@author: js02sixty
'''

from flask import Blueprint
from flask_restful import Api


errors = {
    'IntegrityError': {
        'message': 'Record already exists!',
        'status': 409
    },
    'AttributeError': {
        'message': 'Record not found!',
        'status': 404
    }
}


apiv1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
api = Api(apiv1, errors=errors)

from resources.users import UserListApi, UserApi
from resources.products import (
    ProductListApi,
    ProductApi,
    ProductNoteListApi,
    ProductNoteApi
)
#from resources.notes import NoteApi
from resources.site_initialization import (
    InitializeDB, InitSampleDB)

api.add_resource(InitializeDB, '/initdb')
api.add_resource(InitSampleDB, '/initsampledb')
api.add_resource(UserListApi, '/users')
api.add_resource(UserApi, '/users/<int:user_id>')
api.add_resource(ProductListApi, '/products')
api.add_resource(ProductApi, '/products/<int:product_id>')
api.add_resource(ProductNoteListApi, '/products/<int:product_id>/notes')
api.add_resource(ProductNoteApi, '/products/<int:product_id>/notes/<int:note_id>')
