'''
Created on Apr 6, 2015

@author: js02sixty
'''

from candlemaker.database import db_session
from candlemaker.models import User, UserGroup, Product, Note


def load_default():
    db_session.add_all([
        UserGroup(name='administrators'),
        UserGroup(name='users')
    ])
    db_session.commit()

    g_admins = UserGroup.query.filter(  # @UndefinedVariables
        UserGroup.name == 'administrators').first()  # @UndefinedVariable
    u_admin = User(
        username='admin',
        password='password',
        email='admin@requiescents.com',
        group_id=g_admins.id
    )

    db_session.add_all([u_admin])
    db_session.commit()


def load_sample():
    p1 = Product(name='chamomile',
                 description='This is Chamomile soap',
                 weight=0.65,
                 price=5,
                 pic_url='http://google.com'
                 )
    p1.notes.append(Note(note='This is note #1'))
    p1.notes.append(Note(note='This is note #2'))

    p2 = Product(name='lavender',
                 description='This is a Lavender Candle',
                 weight=1.22,
                 price=23.45,
                 pic_url='http://yahoo.com',
                 )
    p2.notes.append(Note(note='This candle rules!'))
    p2.notes.append(Note(note="It's Purple"))

    db_session.add_all([p1, p2])  # @UndefinedVariable
    db_session.commit()  # @UndefinedVariable
