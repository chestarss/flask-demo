# -*- coding: utf-8 -*-
from flask_restful import Api
from user import *
from server import *

api = Api()
api.add_resource(Ctrl_User, '/api/user')
api.add_resource(Ctrl_Server, '/api/server')
__all__ = ['api']
