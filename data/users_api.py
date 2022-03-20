from flask import jsonify, Blueprint, request
from . import db_session
from .users import User

blueprint = Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'user':
                [user.to_dict(only=('email', 'surname', 'name', 'age', 'speciality'))
                 for user in users]
        }
    )


@blueprint.route('/api/users/<int:users_id>', methods=['GET'])
def get_one_user(users_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(users_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict(only=('email', 'surname', 'name', 'age', 'position', 'speciality', 'address',
                                       'city_from'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['email', 'surname', 'name', 'age', 'position', 'speciality', 'address',
                                                 'password', 'password_again', 'city_from']):
        return jsonify({'error': 'Bad request'})
    if request.json['password'] != request.json['password_again']:
        return jsonify({'error': "Passwords doesn't match"})
    db_sess = db_session.create_session()
    if request.json.get('id') and request.json.get('id') in [user.id for user in db_sess.query(User).all()]:
        return jsonify({'error': 'Id already exists'})
    if request.json.get('email') in [user.email for user in db_sess.query(User).all()]:
        return jsonify({'error': 'Email already exists'})
    user = User()
    if request.json.get('id'):
        user.id = request.json.get('id')
    user.email = request.json['email']
    user.surname = request.json['surname']
    user.name = request.json['name']
    user.age = request.json['age']
    user.position = request.json['position']
    user.speciality = request.json['speciality']
    user.address = request.json['address']
    user.city_from = request.json['city_from']
    user.set_password(request.json['password'])
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_user(users_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(users_id)
    if not user:
        return jsonify({'error': 'Not found'})
    if users_id == 1:
        return jsonify({'error': "you can't delete captain"})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['PUT'])
def redact_user(users_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    if request.json.get('id') and request.json.get('id') in [user.id for user in db_sess.query(User).all()]:
        return jsonify({'error': 'Id already exists'})
    user = db_sess.query(User).get(users_id)
    if not user:
        return jsonify({'error': 'Not found'})
    user.id = request.json['id'] if request.json.get('id') else user.id
    user.email = request.json['email'] if request.json.get('email') else user.email
    user.surname = request.json['surname'] if request.json.get('surname') else user.surname
    user.name = request.json['name'] if request.json.get('name') else user.name
    user.age = request.json['age'] if request.json.get('age') else user.age
    user.position = request.json['position'] if request.json.get('position') else user.position
    user.speciality = request.json['speciality'] if request.json.get('speciality') else user.speciality
    user.city_from = request.json['city_from'] if request.json.get('city_from') else user.city_from
    user.address = request.json['address'] if request.json.get('address') else user.address
    if request.json.get('password'):
        user.set_password(request.json.get('password'))
    db_sess.commit()
    return jsonify({'success': 'OK'})
