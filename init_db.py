# -*- coding: utf-8 -*-
from model.model import *
from sqlalchemy import create_engine
from config.config import SQLALCHEMY_DATABASE_URI

'''
初始化数据库，有表变更的时候调用,或者每次发布时调用
'''
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
