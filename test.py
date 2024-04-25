from aidds_web.utils import get_service_pickle
from aidds_web.utils import app_exception

def mytest():
    try:
        get_service_pickle()
    except Exception as e:
        raise app_exception(e)
    