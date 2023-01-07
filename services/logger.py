import logging
import logging.handlers
import os

from configuration.config import config


def __setup_logger(logger_name):
    log_location = config['logging']['location']
    log_format = "%(asctime)s [%(levelname)-5.5s] %(message)s"
    log_path = os.path.join(log_location, logger_name)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    rotating_file_handler = logging.handlers.RotatingFileHandler(
        log_path,
        maxBytes=(1048576 * 5),
        backupCount=7)
    # log file handler
    log_formatter = logging.Formatter(log_format)
    rotating_file_handler.setFormatter(log_formatter)
    logger.addHandler(rotating_file_handler)
    rotating_file_handler.setLevel(logging.INFO)

    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
    console_handler.setLevel(logging.INFO)
    return logger


logger_name = config['host_service']['name'] + ".log"
logger = __setup_logger(logger_name)
