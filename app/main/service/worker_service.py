import uuid
import datetime

from app.main import db
from app.main.model.healthworker import Worker


def save_new_user(data):
    user = Worker.query.filter_by(email=data['email']).first()
    if not user:
        new_user = Worker(
            name = data['name'],
            email = data['email'],
            admin = data['admin'],
            password = data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return data, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return Worker.query.all()


def get_a_user(id):
    return Worker.query.filter_by(id=id).first()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()