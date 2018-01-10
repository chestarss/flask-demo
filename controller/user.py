from common import Restapi
from model.model import db,User

class Ctrl_User(Restapi):
    def get(self):
        users = db.session.query(User).all()
        result = map(lambda x:x.to_json(), users)
        return result 

__all__ = ['Ctrl_User']
