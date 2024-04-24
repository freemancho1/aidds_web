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