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

_file = {
    'type': {
        'data'                  : 'data',
        'pickle'                : 'pickle',
        # Using: joblib
        'model'                 : 'model',
    },
    'ext': {
        'excel'                 : '.xlsx',
        'csv'                   : '.csv',
        'pickle'                : '.pkl',
        'model'                 : '.model',
    },
    'base_path': \
        os.path.join(os.path.expanduser('~'), 'projects', 'aidds_web', 'xxxx'),
}