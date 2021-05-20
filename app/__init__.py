# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.patient_controller import api as patient_ns
from .main.controller.centre_controller import api as centre_ns
from .main.controller.worker_controller import api as worker_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(patient_ns, path='/patient')
api.add_namespace(centre_ns, path='/heathcentre')
api.add_namespace(worker_ns, path='/healthworker')