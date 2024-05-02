#!/usr/bin.python3
"""defines DBStorage class"""

import models
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlachemy import create_engine


class DBStorage:
    """Connects the app to a database"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        db_url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(user, passwd, host,
                                                           db_name)
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        # Query all objects
        from models.base_model import Base, classes
        objects = {}
        if cls:
            query_result = self.__session.query(classess[cls]).all()
        else:
            for class_name in classes:
                query_result = self.__session.query(classes[class_name]).all()
                for obj in query_result:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
            return objects

        def new(self, obj):
            self.__session.add(obj)

        def save(self):
            self.__session.commit()

        def delete(self, obj=name):
            if obj:
                self.__session.delete(obj)

        def reload(self):
            from models.base_model import Base, classes
            Base.metadata.create_all(self.__engine)
            Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scooped_session(Session)
