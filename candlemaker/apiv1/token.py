'''
Created on June 14, 2015

@author: js02sixty
'''
import jwt
from candlemaker import app
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from candlemaker.models import User
from candlemaker.database import db_session
from candlemaker.apiv1 import auth, group_check


"""
encoded = jwt.encode({'some': 'payload'},
                     app.config['SECRET_KEY'],
                     algorithm='HS256')
"""


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'group_id': fields.Integer
}


parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class GetToken(Resource):

    # @auth.login_required
    # @marshal_with(user_fields)
    def put(self):
        args = parser.parse_args()
        user = User.query.filter(User.Username == username).first()
        if not user or password:
            abort(404)
        user.username = args["username"]
        user.password = args["password"]
        return user, 200
        # return user, 200, {"nonstandard-header": "test"}
