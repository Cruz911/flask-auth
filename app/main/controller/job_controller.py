from flask import request
from flask_restplus import Resource

from ..util.dto import JobDto
from ..service.jobservice import save_new_job, get_a_job_by_district, get_all_jobs, get_a_job

api = JobDto.api
_job = JobDto.user


@api.route('/')
class JobList(Resource):
    @api.doc('list_of_registered_jobs')
    @api.marshal_list_with(_job, envelope='data')
    def get(self):
        """List all registered workers"""
        return get_all_jobs()

    @api.response(201, 'Worker successfully created.')
    @api.doc('create a new worker')
    @api.expect(_job, validate=True)
    def post(self):
        """Creates a new Worker """
        data = request.json
        return save_new_job(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Worker identifier')
@api.response(404, 'Worker not found.')
class User(Resource):
    @api.doc('get a worker')
    @api.marshal_with(_job)
    def get(self, public_id):
        """get a worker given their identifier"""
        user = get_a_job(public_id)
        if not user:
            api.abort(404)
        else:
            return user
        
# get job by district next
