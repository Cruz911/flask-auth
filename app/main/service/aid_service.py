import uuid
import datetime

from app.main import db
from app.main.model.aid import Aid


def save_new_job(data):
    user = Aid.query.filter_by(email=data['email']).first()
    if not user:
        new_user = Aid(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            title=data['title'], 
            description = data['description'],
            status = data['status'],
            no_of_patients = data['no_of_patients'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return new_user, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_jobs():
    return Aid.query.all()


def get_a_job(public_id):
    return Aid.query.filter_by(public_id=public_id).first()

def get_a_job_by_district(district):
    return Aid.query.filter_by(district=district).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()