import os
from dotmap import DotMap
from datetime import datetime

# Settings

# System
_sys = {
    'debug_mode': True,
    # Whether to output logs
    'display_logs': True,
    # Web service
    'web': {
        'port': 11001,
    },
    'utils': {
        'trace': {
            'skip_lib': 'envs',     # No longer in use
            'error_pattern': r'\n[A-Z].*?\n',
        }
    }
}

# Data type
_type = {
    # Provide DataSet
    'pds': ['cons', 'pole', 'line', 'sl'],
    # Training DataSet
    'tds': ['train_x', 'test_x', 'train_y', 'test_y']
}

# Columns
_cols = {
    # Column to be used for joining
    'join'                      : 'acc_no',
    # Column to be used as the target for model training
    'target'                    : 'cons_cost'
}
_cols.update({
    'cons': [
        _cols['join'],
        _cols['target'],  
        'pred_no',
        'pred_type',
        'acc_date',   # Remove
        'office_cd',
        'cont_cap',
        'sup_type',
    ]
})

_file = {
    'type': {
        'data'                  : 'data',
        'pickle'                : 'pickle',
        # Using: joblib
        'model'                 : 'model',
    },
    'ext': {
        'pickle'                : '.pkl',
        'model'                 : '.model',
    },
    'base_path': os.path.join(
        os.path.expanduser('~'), 
        'projects', 'aidds_web', 'data'
    ),
}
_pkl = _file['ext']['pickle']
_model = _file['ext']['model']
_file.update({
    # Memory Data
    'pickle': {
        'office_codes': 'mem01_office_codes'+_pkl,
        'pole_one_hot_cols': 'mem02_pole_one_hot_cols'+_pkl,
        'line_one_hot_cols': 'mem03_line_one_hot_cols'+_pkl,
        'sl_one_hot_cols': 'mem04_sl_one_hot_cols'+_pkl,
        'last_pp_cols': 'mem05_last_pp_cols'+_pkl,
        'modeling_cols': 'mem06_modeling_cols'+_pkl,
        'scaler': 'mem07_scaler'+_pkl,
    },
    # Model Data: 
    # This model data is stored using joblib instead of pickle
    'model': f'mem09_model_best'+_model,
})

# Constraints on modeling data
_constraints = {
    'acc_type_name'             : '신설(상용/임시)',
    'max_cont_cap'              : 50,
    'cons_type_cd'              : 2,
    'max_total_cons_cost'       : 30000000,
    'min_pole_cnt'              : 0,
    'max_pole_cnt'              : 10,
    'min_line_cnt'              : 0,
    'max_line_cnt'              : 11,
    'sl_cnt'                    : 1,
} 

# Convert dictionary to semi-class
# - to use attribute assignment, e.g., sys.cond.debug_mode = False
sys = DotMap(_sys)
type = DotMap(_type)
cols = DotMap(_cols)
file = DotMap(_file)
constraints = DotMap(_constraints)