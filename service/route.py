from flask import jsonify, request, json, abort
from flask.views import MethodView
from werkzeug.exceptions import HTTPException

from aidds_web.sys import http_codes as hc
from aidds_web.utils import app_exception
from aidds_web.utils import route_error_handle
from aidds_web.service import service_manager

sm = service_manager().get_instance()


class PredictRoute(MethodView):
    
    def post(self):
        try:
            # Exception handling is ambiguous
            # input_json = request.json
            input_data = request.get_data()
            input_json = json.loads(input_data)
        except ValueError as ve:
            return route_error_handle('web.bad_json', str(ve), hc.BR, ve)
        
        try:
            ret_json = sm.predict().run(in_json=input_json)
            return ret_json, hc.OK
        except HTTPException as he:
            return route_error_handle(f'hc_msg.e{he.code}', None, he.code, he)
        except app_exception as ae:
            return route_error_handle('hc_msg.e500', None, hc.ISE, ae)
        except Exception as e:
            return route_error_handle('hc_msg.e500', None, hc.ISE, e)
        

class RePredictRoute(MethodView):
    
    def post(self):
        try:
            # Exception handling is ambiguous
            # input_json = request.json
            input_data = request.get_data()
            input_json = json.loads(input_data)
        except ValueError as ve:
            return route_error_handle('web.bad_json', str(ve), hc.BR, ve)
        
        try:
            # Test HTTPException
            # abort(401)
            ret_json = sm.predict().run(in_json=input_json)
            # Leave only 'cons' item and remove all the remaining items
            ret_json = json.loads(ret_json)
            pred_id = next(iter(ret_json))
            cons = ret_json[pred_id].get('cons', {})
            ret_json = json.dumps(cons)
            return ret_json, hc.OK
        except HTTPException as he:
            return route_error_handle(f'hc_msg.e{he.code}', None, he.code, he)
        except app_exception as ae:
            return route_error_handle('hc_msg.e500', None, hc.ISE, ae)
        except Exception as e:
            return route_error_handle('hc_msg.e500', None, hc.ISE, e)