'''
Created on Apr 6, 2015

@author: js02sixty
'''
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from candlemaker.models import UserGroup
from candlemaker.database import db_session
# from candlemaker.apiv1 import auth, group_check


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'createdby': fields.String,
    'editedby': fields.String,
    'created': fields.DateTime,
    'edited': fields.DateTime
}

user_group_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'createdby': fields.String,
    'editedby': fields.String,
    'created': fields.DateTime,
    'edited': fields.DateTime,
    'users': fields.Nested(user_fields)
}


parser = reqparse.RequestParser()
parser.add_argument('name', type=str)


class UserGroupListApi(Resource):

    @marshal_with(user_group_fields)
    def get(self):
        user_group = UserGroup.query.all()
        return user_group


    @marshal_with(user_group_fields)
    def post(self):
        """May decide latter to remove posting of new groups."""
        args = parser.parse_args()
        user_group = UserGroup()
        user_group.name = args['name']
        user_group.createdby = auth.username()
        db_session.add(user_group)
        db_session.commit()
        return user_group, 201



class UserGroupApi(Resource):

    @marshal_with(user_group_fields)
    def get(self, user_group_id):
        user_group = UserGroup.query.filter(
            UserGroup.id == user_group_id).first()
        if not user_group:
            abort(404)
        return user_group
