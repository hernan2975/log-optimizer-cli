# logger.py

import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

def setup_logger(log_file_path=None):
    """Configura el logger principal para la CLI"""
    logger = logging.getLogger('log_optimizer')
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        return logger  # Evita duplicación de handlers si se reutiliza

    # Log por defecto a stdout si no se indica un archivo
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    if log_file_path:
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        handler = RotatingFileHandler(
            log_file_path,
            maxBytes=5 * 1024 * 1024,  # 5MB
            backupCount=3
        )
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

