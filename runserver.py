from app import MyAPP
from model.model import db
from controller.controller import api
from config import config
app = MyAPP(__name__, config)
app.init_db(db)
app.init_api(api)
app.run()
