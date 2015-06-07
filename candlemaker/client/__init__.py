'''
Created on Apr 12, 2015

@author: js02sixty
'''

from flask import Blueprint

client = Blueprint('home', __name__, static_folder='app', static_url_path='')


@client.route('/')
@client.route('/admin')
@client.route('/products')
@client.route('/about')
@client.route('/contact')
def index():
    return client.send_static_file('index.html')
