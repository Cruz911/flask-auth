import uuid
import datetime

from app.main import db
from app.main.model.job import Job


def save_new_job(data):
    user = Job.query.filter_by(email=data['email']).first()
    if not user:
        new_user = Job(
            email=data['email'],
            title=data['title'], 
            description = data['description'],
            status = data['status'],
            district=data['district'],
            no_of_patients = data['no_of_patients'],
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


def get_all_jobs():
    return Job.query.all()


def get_a_job(id):
    return Job.query.filter_by(id=id).first()

def get_a_job_by_district(district):
    return Job.query.filter_by(district=district).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()