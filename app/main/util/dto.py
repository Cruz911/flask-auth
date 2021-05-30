from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
    
class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    
class PatientDto:
    api = Namespace('patient', description='patient related operations')
    user = api.model('patient', {
        'password': fields.String(required=True, description='user password'),
        'email' : fields.String(required=True, description='patient email'),
        'name' : fields.String(required=True, description='patient name'),
        'age' :fields.Integer(required=True, description='patient age'),
        'sex' : fields.String(required=True, description='patient sex'),
        'address' :fields.String(required=True, description='patient address'),
        'district' : fields.String(required=True, description='patient district'),
        'phone_number' : fields.Integer(required=True, description='patient number'),
        'diagnosis' : fields.String(required=True, description='patient diagnosis'),
        'plan' :fields.String(required=True, description='patient plan'),
        'complaints' :fields.String(required=True, description='patient complaints'),
        'allergies' :fields.String(required=True, description='patient allergies'),
        'occupation' : fields.String(required=True, description='patient occupation'),
        'marital_status' : fields.String(required=True, description='patient marital status'),
        'aid' : fields.Boolean(required=True, description='patient aid'),
        'job' : fields.Boolean(required=True, description='patient job')
    })
    
class WorkerDto:
    api = Namespace('healthworker', description='healthworker related operations')
    user = api.model('healthworker', {
        'email': fields.String(required=True, description='worker email address'),
        'name': fields.String(required=True, description='worker username'),
        'password': fields.String(required=True, description='worker password'),
        'admin': fields.Boolean(required=True, description='worker admin status')

    })
    
class CentreDto:
    api = Namespace('healthcentre', description='healthcentre related operations')
    user = api.model('healthcentre', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })
    
class JobDto:
    api = Namespace('job', description='jobcentre related operations')
    user = api.model('job', {
        'email': fields.String(required=True, description='user email address'),
        'title': fields.String(requred=True, description='job title'),
        'description': fields.String(requred=True, description='job description'),
        'status': fields.String(requred=True, description='job status'),
        'district': fields.String(requred=True, description='district'),
        'no_of_patients': fields.Integer(requred=True, description='required number')

    })
    
class AidDto:
    api = Namespace('aid', description='aid and donations related operations')
    user = api.model('aid', {
        'email': fields.String(required=True, description='user email address'),
        'title': fields.String(requred=True, description='job title'),
        'description': fields.String(requred=True, description='job description'),
        'status': fields.String(requred=True, description='job status'),
        'district': fields.String(requred=True, description='district'),
        'no_of_patients': fields.Integer(requred=True, description='required number')
    })
