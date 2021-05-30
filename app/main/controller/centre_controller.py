from flask import request
from flask_restplus import Resource

from ..util.dto import CentreDto
from ..service.centre_service import save_new_user, get_all_users, get_a_user

api = CentreDto.api
_user = CentreDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_centres')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered centres"""
        return get_all_users()

    @api.response(201, 'Centre successfully created.')
    @api.doc('create a new centre')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new Centre """
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'The Centre identifier')
@api.response(404, 'Centre not found.')
class User(Resource):
    @api.doc('get a centre')
    @api.marshal_with(_user)
    def get(self, id):
        """get a centre given its identifier"""
        user = get_a_user(id)
        if not user:
            api.abort(404)
        else:
            return user