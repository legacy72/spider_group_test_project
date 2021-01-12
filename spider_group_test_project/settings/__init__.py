import logging

from .settings import *

try:
    from .local_settings import *
except ImportError:
    logging.info('Локальные настройки не импортированы')
