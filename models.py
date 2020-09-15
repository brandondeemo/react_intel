from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.__init__(app)


class User(db.Model):
    __tablename__='Type'
    Type_id = db.Column('Type_id',db.Integer,primary_key=True,nullable=False)
    Type_name = db.Column('Type_name',db.VARCHAR(45),nullable=False)

    def __init__(self,Type_id,Type_name):
        self.Type_id=Type_id
        self.Type_name=Type_name


class Person(db.Model):
    __tablename__='Person'
    person_id = db.Column('person_id',db.VARCHAR(20),primary_key=True,nullable=False)
    password = db.Column('password',db.VARCHAR(45),nullable=False)
    person_type = db.Column('person_type',db.VARCHAR(10),nullable=False)
    email = db.Column('email',db.VARCHAR(45),nullable=False)

    def __init__(self,person_id,password,person_type,email):
        self.person_id=person_id
        self.password=password
        self.person_type=person_type
        self.email=email

