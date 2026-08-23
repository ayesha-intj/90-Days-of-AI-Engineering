import logging
from logging.handlers import RotatingFileHandler

def configure_logger(logs_path):
     # Setup Logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    
    # Attach Stream Handler (Console output)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    # Attach Rotating File Handler (File output)
    log_file_handler = RotatingFileHandler(logs_path, maxBytes=50000, backupCount=2, encoding="utf-8")
    log_file_handler.setLevel(logging.DEBUG)
    log_file_handler.setFormatter(formatter)
    logger.addHandler(log_file_handler)
