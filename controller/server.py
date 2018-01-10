from common import Restapi
from model.model import db, Server

class Ctrl_Server(Restapi):
    def get(self):
        servers = db.session.query(Server).all()
        result = map(lambda x:x.to_json(), servers)
        return result 

__all__ = ['Ctrl_Server']
