import dags.scripts.config as config
import uuid
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


class Connection(object):
    def __init__(self):
        # create a db connection
        engine = create_engine()
        self.engine = engine

    def get_session(self):
        Session = sessionmaker(bind=self.engine)

        return Session()

    def get_engine(self):
        return self.engine


Base = declarative_base()


def init_db():
    # create a db connection
    engine = create_engine()
    Base.metadata.create_all(bind=engine)

class Users(Base):
    __tablename__ = 'users'

	# define required database columes

    def __init__(self, name, age):
        # init database model
        pass
