import os

import cherrypy
from jinja2 import Environment, FileSystemLoader

abc123;;

ENV = Environment(loader=FileSystemLoader('templates'))


def get_params():
    params = {'key': os.environ.get('key', ''),
              'user': os.environ.get('user', ''),
              'password': os.environ.get('password', '')}
    return params


class Root(object):
    @cherrypy.expose
    def index(self):
        tmpl = ENV.get_template('index.html')
        params = get_params()
        return tmpl.render(params)

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 80})

cherrypy.quickstart(Root())
