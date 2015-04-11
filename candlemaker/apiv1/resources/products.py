'''
Created on Apr 8, 2015

@author: js02sixty
'''
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from candlemaker.models import Product, Note
from candlemaker.database import db_session


note_fields = {
    'id': fields.Integer,
    'note': fields.String,
    'created': fields.DateTime,
    'edited': fields.DateTime
}

product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'notes': fields.Nested(note_fields),
    'weight': fields.Fixed(decimals=4),
    'price': fields.Fixed(decimals=2),
    'pic_url': fields.String,
    'category_id': fields.Integer,
    'created': fields.DateTime,
    'edited': fields.DateTime
}

product_parser = reqparse.RequestParser()
product_parser.add_argument('name', type=str)
product_parser.add_argument('description', type=str)
product_parser.add_argument('notes', type=str, action='append')
product_parser.add_argument('weight', type=float)
product_parser.add_argument('price', type=float)
product_parser.add_argument('pic_url', type=str)
product_parser.add_argument('category_id', type=int)

note_parser = reqparse.RequestParser()
note_parser.add_argument('note', type=str)


class ProductListApi(Resource):

    @marshal_with(product_fields)
    def get(self):
        user = Product.query.all()  # @UndefinedVariable
        return user

    @marshal_with(product_fields)
    def post(self):
        args = product_parser.parse_args()
        product = Product(
            name=args['name'],
            description=args['description'],
            weight=args['weight'],
            price=args['price'],
            pic_url=args['pic_url'],
            category_id=args['category_id']
        )
        db_session.add(product)
        db_session.commit()
        return product, 201


class ProductApi(Resource):

    @marshal_with(product_fields)
    def get(self, product_id):
        product = Product.query.filter(  # @UndefinedVariable
            Product.id == product_id).first()  # @UndefinedVariable
        if not product:
            abort(404, message="Product {} doesn't exist".format(product_id))
        return product

    def delete(self, product_id):
        product = Product.query.filter(  # @UndefinedVariable
            Product.id == product_id).first()  # @UndefinedVariable
        if not product:
            abort(404, message="Product {} doesn't exist".format(product_id))
        db_session.delete(product)
        db_session.commit()
        return {}, 204

    @marshal_with(product_fields)
    def put(self, product_id):
        args = product_parser.parse_args()
        product = Product.query.filter(  # @UndefinedVariable
            Product.id == product_id).first()  # @UndefinedVariable
        if not product:
            abort(404, message="Product {} doesn't exist".format(product_id))
        product.name = args['name']
        product.description = args['description'],
        product.weight = args['weight']
        product.price = args['price']
        product.pic_url = args['pic_url']
        product.category_id = args['category_id']
        db_session.add(product)
        db_session.commit()
        return product, 201


class ProductNoteListApi(Resource):

    @marshal_with(note_fields)
    def get(self, product_id):
        product = Product.query.filter(  # @UndefinedVariable
            Product.id == product_id).first()  # @UndefinedVariable
        if not product:
            abort(404, message="Product {} doesn't exist".format(product_id))
        return product.notes

    @marshal_with(note_fields)
    def post(self, product_id):
        args = note_parser.parse_args()
        note = Note(note=args['note'])
        product = Product.query.filter(  # @UndefinedVariable
            Product.id == product_id).first()  # @UndefinedVariable
        if not product:
            abort(404, message="Product {} doesn't exist".format(product_id))
        product.notes.append(note)
        db_session.add(product)
        db_session.commit()
        return note, 201


class ProductNoteApi(Resource):

    @marshal_with(note_fields)
    def get(self, product_id, note_id):
        product = Product.query.filter(  # @UndefinedVariable
            Product.id == product_id).first()  # @UndefinedVariable
        if not product:
            abort(404, message="Product {} doesn't exist".format(product_id))
        note = Note.query.filter(Note.id == note_id).first()  # @UndefinedVariable
        if not note:
            abort(404, message="Note {} doesn't exist".format(note_id))
        return note

    def delete(self, product_id, note_id):
        product = Product.query.filter(  # @UndefinedVariable
            Product.id == product_id).first()  # @UndefinedVariable
        if not product:
            abort(404, message="Product {} doesn't exist".format(product_id))
        note = Note.query.filter(Note.id == note_id).first()  # @UndefinedVariable
        if not note:
            abort(404, message="Note {} doesn't exist".format(note_id))
        product.notes.remove(note)
        db_session.commit()
        return {}, 204

    @marshal_with(note_fields)
    def put(self, product_id, note_id):
        args = note_parser.parse_args()
        product = Product.query.filter(  # @UndefinedVariable
            Product.id == product_id).first()  # @UndefinedVariable
        if not product:
            abort(404, message="Product {} doesn't exist".format(product_id))
        note = Note.query.filter(Note.id == note_id).first()  # @UndefinedVariable
        if not note:
            abort(404, message="Note {} doesn't exist".format(note_id))
        note.note = args['note']
        db_session.add(note)
        db_session.commit()
        return note, 201
