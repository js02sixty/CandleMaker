'''
Created on Apr 6, 2015

@author: js02sixty
'''
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from candlemaker.models import User
from candlemaker.database import db_session
from candlemaker.apiv1 import auth, group_check


user_group_fields = {
    'id': fields.Integer,
    'name': fields.String
}

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'group_id': fields.Integer,
    'createdby': fields.String,
    'editedby': fields.String,
    'created': fields.DateTime,
    'edited': fields.DateTime
}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)
parser.add_argument('first_name', type=str)
parser.add_argument('last_name', type=str)
parser.add_argument('email', type=str)
parser.add_argument('group_id', type=int)


class UserListApi(Resource):

    @marshal_with(user_fields)
    def get(self):
        user = User.query.all()  # @UndefinedVariable
        return user

    @auth.login_required
    @marshal_with(user_fields)
    def post(self):
        if group_check(auth.username(), 'administrators'):
            args = parser.parse_args()
            user = User(
                username = args['username'],
                password = args['password'],
                first_name = args['first_name'],
                last_name = args['last_name'],
                email = args['email'],
                group_id = args['group_id'],
                createdby = auth.username()
            )
            db_session.add(user)  # @UndefinedVariable
            db_session.commit()  # @UndefinedVariable
            return user, 201
        else:
            abort(401)


class UserApi(Resource):

    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.query.filter(User.id == user_id).first()  # @UndefinedVariable
        if not user:
            abort(404)
        return user

    def delete(self, user_id):
        if group_check(auth.username(), 'administrators'):
            user = User.query.filter(User.id == user_id).first()  # @UndefinedVariable
            if not user:
                abort(404)
            db_session.delete(user)  # @UndefinedVariable
            db_session.commit()  # @UndefinedVariable
            return {}, 204
        else:
            abort(401)

    @marshal_with(user_fields)
    def put(self, user_id):
        if group_check(auth.username(), 'administrators'):
            args = parser.parse_args()
            user = User.query.filter(User.id == user_id).first()  # @UndefinedVariable
            if not user:
                abort(404)
            user.username = args["username"]
            user.password = args["password"]
            user.first_name = args["first_name"]
            user.last_name = args["last_name"]
            user.email = args["email"]
            user.group_id = args["group_id"]
            user.editedby = auth.username()
            db_session.add(user)  # @UndefinedVariable
            db_session.commit()  # @UndefinedVariable
            return user, 201
        else:
            abort(401)
