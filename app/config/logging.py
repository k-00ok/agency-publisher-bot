from __future__ import annotations

import logging

LOGGER_NAME='agency_publisher'
FORMAT='%(asctime)s | %(levelname)s | %(name)s | %(message)s'


def setup_logging()->logging.Logger:
    logger=logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    handler=logging.StreamHandler()
    handler.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(handler)
    logger.propagate=False
    return logger
