import numpy as np
from flask import jsonify
from aidds_web import messages as msg
from aidds_web.utils import route_error_logs as logs
from aidds_web.utils import app_exception


def convert_to_builtin_int(obj):
    # If object type np.int64, converted to a Python int
    return int(obj) if isinstance(obj, np.int64) else obj

def convert_to_builtin_float(obj):
    # If object type np.float64, converted to a Python float
    return float(obj) if isinstance(obj, np.float64) else obj

def mean_absolute_percentage_error(y:any, p:any) -> any:
    return abs((y-p) / y) * 100

def route_error_handle(
    code=None, 
    value=None, 
    status_code=None,
    error_obj=None
):
    if isinstance(error_obj, app_exception):
        error_obj.print()
    else:
        logs(error_obj)
    error_message = eval(f'msg.exception.{code}')
    error_message += '' if value is None else f': {value}'
    return jsonify({'error': error_message}), status_code