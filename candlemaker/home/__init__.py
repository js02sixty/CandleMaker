'''
Created on Apr 6, 2015

@author: js02sixty
'''

from flask import Blueprint

home = Blueprint('home', __name__, static_folder='static', static_url_path='')


@home.route('/')
@home.route('/admin')
@home.route('/products')
@home.route('/about')
@home.route('/contact')
def index():
    return home.send_static_file('index.html')
