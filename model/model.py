# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.inspection import inspect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()

#model 基类，用于增加一些公共方法
class baseMixin(object):
    
    def _to_json(self):
        '''
        表字段遍历转json
        '''
        columns = self.__class__.__table__.columns.keys()
        try:
            hide_columns = getattr(self,'_json_hide_columns')
            if hide_columns:
                columns = list(set(columns) - set(hide_columns))    
        except:
            pass
        rs = {}
        for c in columns:
            rs[c] = getattr(self,c)
        return rs
    def to_json(self):
        '''
        表relationship字段遍历转json
        '''
        rs = self._to_json()
        relationship_columns = inspect(self.__class__).relationships.keys()
        for rc in relationship_columns:
            rc_obj = getattr(self,rc)
            if isinstance(rc_obj,list):
                rs[rc] = map(lambda x:x._to_json(),rc_obj)
            elif isinstance(rc_obj.__class__,Base):
                rs[rc] = rc_obj._to_json()
        return rs

class User(baseMixin, Base):
    __tablename__ = 'user'
    # 敏感字段可以这样配置不在json中显示
    _json_hide_columns = ['password']

    id = Column(Integer,primary_key=True)
    #所有字段需要显式指定长度，create_all需要
    username = Column(String(64),nullable=False,index=True)
    password = Column(String(64),nullable=False)
    email = Column(String(128),nullable=False,index=True)
    servers = relationship('Server',secondary='resource_owner',backref='users')
    
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class Server(baseMixin, Base):
    __tablename__ = 'server'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),nullable=False,index=True)

    def __init__(self,hostname):
        self.hostname = hostname

class Resource_Owner(Base):
    __tablename__ = 'resource_owner'
    id = Column(Integer,primary_key =True)
    user_id = Column(Integer,ForeignKey('user.id'))
    server_id = Column(Integer,ForeignKey('server.id'))

