import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    dialect = 'mysql'
    driver = 'pymysql'
    username = 'root'
    password = 'sunjian8844'
    host = 'localhost'
    port = '3306'
    database = 'Intel'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
        dialect, driver,username, password, host, port, database)

    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
