import os

import cherrypy
from jinja2 import Environment, FileSystemLoader


ENV = Environment(loader=FileSystemLoader('templates'))


def get_params():
    params1 = {'key1': os.environ.get('key', ''),
               'user1': os.environ.get('user', ''),
               'password1': os.environ.get('password', '')}
    return params1


class Root(object):
    @cherrypy.expose
    def index(self):
        tmpl = ENV.get_template('index.html')
        params = get_params()
        return tmpl.render(params)

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 80})

cherrypy.quickstart(Root())
