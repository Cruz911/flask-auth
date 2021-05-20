from flask import request
from flask_restplus import Resource

from ..util.dto import WorkerDto
from ..service.worker_service import save_new_user, get_all_users, get_a_user

api = WorkerDto.api
_worker = WorkerDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_workers')
    @api.marshal_list_with(_worker, envelope='data')
    def get(self):
        """List all registered workers"""
        return get_all_users()

    @api.response(201, 'Worker successfully created.')
    @api.doc('create a new worker')
    @api.expect(_worker, validate=True)
    def post(self):
        """Creates a new Worker """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Worker identifier')
@api.response(404, 'Worker not found.')
class User(Resource):
    @api.doc('get a worker')
    @api.marshal_with(_worker)
    def get(self, public_id):
        """get a worker given their identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user