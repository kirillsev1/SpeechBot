"""File with logger."""
import logging
from config import FORMAT, LOG_PATH
import os
from datetime import datetime


def init_logger(name):
    """Function which initialises logger.

    Args:
        name (str): name of application in log file.
    """
    logger = logging.getLogger(name)
    date_now = datetime.now().date()

    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)

    logging.basicConfig(level=logging.INFO, filename=f"{LOG_PATH}{date_now}.log", filemode="w", format=FORMAT)
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
    logger.debug('logger was initialized')
