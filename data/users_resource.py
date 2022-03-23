from flask import jsonify, request
from flask_restful import abort, Resource
from . import db_session, my_parsers
from .users import User

parser = my_parsers.UserParser()


def abort_if_user_not_found(users_id):
    session = db_session.create_session()
    news = session.query(User).get(users_id)
    if not news:
        abort(404, message=f"User {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_user_not_found(users_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(users_id)
        return jsonify({'user': user.to_dict(only=('email', 'surname', 'name', 'age',
                                                   'position', 'speciality', 'address', 'city_from'))})

    def delete(self, users_id):
        abort_if_user_not_found(users_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(users_id)
        if users_id == 1:
            return jsonify({'error': "you can't delete captain"})
        db_sess.delete(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self, users_id):
        abort_if_user_not_found(users_id)
        if not request.json:
            return jsonify({'error': 'Empty request'})
        db_sess = db_session.create_session()
        if request.json.get('id') and request.json.get('id') in [user.id for user in db_sess.query(User).all()]:
            return jsonify({'error': 'Id already exists'})
        if request.json.get('email') and request.json.get('email') in [user.email for user
                                                                       in db_sess.query(User).all()]:
            return jsonify({'error': 'email already exists'})
        user = db_sess.query(User).get(users_id)
        user.id = request.json['id'] if request.json.get('id') else user.id
        user.email = request.json['email'] if request.json.get('email') else user.email
        user.surname = request.json['surname'] if request.json.get('surname') else user.surname
        user.name = request.json['name'] if request.json.get('name') else user.name
        user.age = request.json['age'] if request.json.get('age') else user.age
        user.position = request.json['position'] if request.json.get('position') else user.position
        user.speciality = request.json['speciality'] if request.json.get('speciality') else user.speciality
        user.city_from = request.json['city_from'] if request.json.get('city_from') else user.city_from
        user.address = request.json['address'] if request.json.get('address') else user.address
        if request.json.get('password') and request.json.get('password_again'):
            if request.json['password'] != request.json['password_again']:
                return jsonify({'error': "Passwords doesn't match"})
            user.set_password(request.json.get('password'))
        elif request.json.get('password') or request.json.get('password_again'):
            return jsonify({'error': "Requires both of 'password' and 'password again' or none of them"})
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify({'user': [user.to_dict(only=('email', 'surname', 'name', 'age', 'speciality'))
                                 for user in users]})

    def post(self):
        args = parser.parse_args()
        if request.json['password'] != request.json['password_again']:
            return jsonify({'error': "Passwords doesn't match"})
        db_sess = db_session.create_session()
        if request.json.get('id') and request.json.get('id') in [user.id for user in db_sess.query(User).all()]:
            return jsonify({'error': 'Id already exists'})
        if request.json.get('email') in [user.email for user in db_sess.query(User).all()]:
            return jsonify({'error': 'Email already exists'})

        user = User()
        if args.get('id'):
            user.id = args.get('id')
        user.email = args['email']
        user.surname = args['surname']
        user.name = args['name']
        user.age = args['age']
        user.position = args['position']
        user.speciality = args['speciality']
        user.address = args['address']
        user.city_from = args['city_from']
        user.set_password(args['password'])

        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK'})
