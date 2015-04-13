'''
Created on Apr 6, 2015

@author: js02sixty
'''

from candlemaker.database import db_session
from candlemaker.models import User, UserGroup, Product, Note, SiteSettings


def load_default():
    db_session.add_all([  # @UndefinedVariable
        UserGroup(name='administrators'),
        UserGroup(name='users'),
        SiteSettings(items_per_page=20)
    ])
    db_session.commit()  # @UndefinedVariable

    g_admins = UserGroup.query.filter(  # @UndefinedVariables
        UserGroup.name == 'administrators').first()  # @UndefinedVariable
    g_users = UserGroup.query.filter(  # @UndefinedVariable
        UserGroup.name == 'users').first()  # @UndefinedVariable
        
    u_admin = User(
        username='admin',
        password='password',
        email='admin@requiescents.com',
        group_id=g_admins.id,
        createdby='admin'
    )
    u_john = User(
        username='john',
        first_name='John',
        last_name='Saba',
        password='password',
        email='js02sixty@gmail.com',
        group_id=g_users.id,
        createdby='admin'
    )

    db_session.add_all([u_admin, u_john])  # @UndefinedVariable
    db_session.commit()  # @UndefinedVariable


def load_sample():
    p1 = Product(name='chamomile',
                 description='This is Chamomile soap',
                 weight=0.65,
                 price=5,
                 pic_url='http://google.com',
                 createdby='admin'
                 )
    p1.notes.append(Note(note='This is note #1'))
    p1.notes.append(Note(note='This is note #2'))

    p2 = Product(name='lavender',
                 description='This is a Lavender Candle',
                 weight=1.22,
                 price=23.45,
                 pic_url='http://yahoo.com',
                 createdby='admin'
                 )
    p2.notes.append(Note(note='This candle rules!'))
    p2.notes.append(Note(note="It's Purple"))

    db_session.add_all([p1, p2])  # @UndefinedVariable
    db_session.commit()  # @UndefinedVariable
