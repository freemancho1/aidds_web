import os
import pandas as pd
from datetime import datetime
from pickle import load as pickle_load
from joblib import load as joblib_load

from aidds_web import config as cfg 
from aidds_web import messages as msg 
from aidds_web.utils import app_exception


def read_data(code:str=None) -> bytes:
    try:
        file_type, file_path, file_ext = _get_file_path(code=code)
        if file_type == cfg.file.type.pickle:
            with open(file_path, 'rb') as file:
                return pickle_load(file)
        if file_type == cfg.file.type.model:
            return joblib_load(file_path)
    except Exception as e:
        raise app_exception(e)
    
def get_service_pickle() -> tuple[dict[str, bytes], bytes, bytes]:
    try:
        pkl = {
            pkey: read_data(code=f'pickle.{pkey}') \
                for pkey in list(cfg.file.pickle.keys())[:-1]
        }
        scaler = read_data(code='pickle.scaler')
        model = read_data(code='model')
        return pkl, scaler, model
    except Exception as e:
        raise app_exception(e)


def _get_file_path(code:str=None) -> tuple[str, str, str]:
    try:
        # Find file name and ext
        file_name = eval(f'cfg.file.{code}')
        _, file_ext = os.path.splitext(file_name)
        
        # Get file type
        assert file_ext.lower() in [cfg.file.ext.pickle, cfg.file.ext.model], \
            f'{msg.exception.sys.unknown_file_ext} "{file_ext}"'
        file_type = cfg.file.type.pickle \
            if file_ext == cfg.file.ext.pickle else cfg.file.type.model
        
        # Get file path list
        file_paths = [cfg.file.base_path, file_type, file_name]
        #      file_type, file_path,                 file_ext
        return file_type, os.path.join(*file_paths), file_ext
    except Exception as e:
        raise app_exception(e)