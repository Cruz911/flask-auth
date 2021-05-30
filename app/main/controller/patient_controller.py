from flask import request
from flask_restplus import Resource

from ..util.dto import PatientDto
from ..service.patient_service import save_new_user, get_all_users, get_a_user

api = PatientDto.api
_patient = PatientDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_patients')
    @api.marshal_list_with(_patient, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'Patient successfully created.')
    @api.doc('create a new patient')
    @api.expect(_patient, validate=True)
    def post(self):
        """Creates a new Patient """
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'The Patient identifier')
@api.response(404, 'Patient not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_patient)
    def get(self, id):
        """get a patient given their identifier"""
        user = get_a_user(id)
        if not user:
            api.abort(404)
        else:
            return user