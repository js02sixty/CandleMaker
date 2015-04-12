'''
Created on Apr 9, 2015

@author: js02sixty
'''
from flask_restful import Resource, fields, marshal_with, reqparse
from candlemaker.models import Note
from candlemaker.database import db_session


note_fields = {
    'id': fields.Integer,
    'note': fields.String,
    'created': fields.DateTime,
    'edited': fields.DateTime
}

note_parser = reqparse.RequestParser()
note_parser.add_argument('note', type=str)


class NoteApi(Resource):

    @marshal_with(note_fields)
    def get(self, note_id):
        note = Note.query.filter(  # @UndefinedVariable
            Note.id == note_id).first()  # @UndefinedVariable
        if not note:
            abort(404)  # @UndefinedVariable            
        return note
    
    def delete(self, note_id):
        note = Note.query.filter(  # @UndefinedVariable
            Note.id == note_id).first()  # @UndefinedVariable
        if not note:
            abort(404)  # @UndefinedVariable
        db_session.delete(note)
        db_session.commit()
        return {}, 204
    
    @marshal_with(note_fields)
    def put(self, note_id):
        args = note_parser.parse_args()
        note = Note.query.filter(  # @UndefinedVariable
            Note.id == note_id).first()  # @UndefinedVariable
        if not note:
            abort(404)  # @UndefinedVariable
        note.note = args['note']
        db_session.add(note)
        db_session.commit()
        return note, 201
    