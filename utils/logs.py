from datetime import datetime

from aidds_web import config as cfg
from aidds_web import message as msg 
from aidds_web.utils import get_caller
from aidds_web.utils import get_error


def service_logs(code:str=None, value:Any=None) -> None:
    """ Logs display function for the service section. """
    if not cfg.sys.display_logs:
        return
    display = f'[{datetime.now()}]'
    display += f' {eval(f"msg.log.service.{code}")}' if code else ''
    display += '' if value is None else f' {value}'
    print(display)
    
    
def route_error_logs(error:Any=None) -> None:
    """ Logs display function for the route errors. """
    head_message = msg.exception.sys.head_message
    display = f'\n[{datetime.now()}]'
    display += f'{head_message}[{get_caller()}]\n{get_error(str(error))}\n'
    print(display)