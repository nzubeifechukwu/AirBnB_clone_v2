#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""


class DBStorage:
    """Database storage class using mysqldb and sqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage module"""
        HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
        HBNB_ENV = os.environ.get('HBNB_ENV')

        self.__engine = create_engine(f"""mysql+mysqldb://{HBNB_MYSQL_USER}:{
                HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{
                HBNB_MYSQL_DB}""", pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)
