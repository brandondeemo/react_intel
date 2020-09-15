from flask import Flask,render_template,request,jsonify,make_response,Blueprint


blue = Blueprint('first_blue',__name__)
from models import db,User,Person



@blue.route('/user', methods=['GET'])
def get_all_users():
    users = Person.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['password'] = user.password
        user_data['person_id'] = user.person_id
        user_data['person_type'] = user.person_type
        user_data['email'] = user.email
        output.append(user_data)

    return jsonify({'users': output})


@blue.route('/user/<user_id>', methods=['GET'])
def get_one_users(user_id):
    user = Person.query.filter_by(person_id=user_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    user_data = {}
    user_data['password'] = user.password
    user_data['person_id'] = user.person_id
    user_data['person_type'] = user.person_type
    user_data['email'] = user.email

    return jsonify({'user': user_data})


@blue.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = Person(data['person_id'], data['password'], data['person_type'], data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'new user created!'})


@blue.route('/user/<user_id>', methods=['PUT'])
def promote_user():
    return ''


@blue.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Person.query.filter_by(person_id=user_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'The user has been deleted'})


@blue.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Counld not verify', 401, {'WWW-Authenticate': 'Basic realm = "Login required!"'})

    user = Person.query.filter_by(name=auth.username).first()
    if not user:
        return make_response('Counld not verify', 401, {'WWW-Authenticate': 'Basic realm = "Login required!"'})


@blue.route('/')
def index():
    return render_template('index.html')
