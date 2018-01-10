from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root:westos@localhost:3306/study_orm?charset=utf8')
Session = sessionmaker(bind=engine)

sess = Session()
users = sess.query(User).all()
print map(lambda x:x.to_json(),users)
