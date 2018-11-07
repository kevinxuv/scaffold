# -*- coding: utf-8 -*-
import os
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

current_path = os.path.dirname(os.path.realpath(__file__))
