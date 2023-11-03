
from flask_restful import abort

def error(message, error_code):
    abort(error_code, message=message)

def invalid_parameter_error(parameter, field):
    error(f'Invalid parameter {parameter} for field {field}!', 400)

def default_already_created_warning(obj):
    print(f'Default {obj} already created!')
    return 200

def already_exists_error(parameter, field, obj):
    error(f'Parameter {parameter} for field {field} of {obj} should be unique!', 400)

def not_found_error(parameter, field, obj):
    error(f'{obj} with {field}: {parameter} not found!', 404)
