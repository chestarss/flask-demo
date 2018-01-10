# -*- coding: utf-8 -*-
from flask import Flask

class MyAPP(Flask):
    def __init__(self, app_name, config_obj):
        Flask.__init__(self, app_name)
        # load config
        self._load_config(config_obj)

    def _load_config(self, config_obj):
        self.config.from_object(config_obj)

    def init_db(self,db):
        self.db = db.init_app(self) 

    def init_api(self,api):
        self.api =  api.init_app(self)
