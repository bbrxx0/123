import logging
from logging.handlers import RotatingFileHandler
from flask import current_app

def get_admin_logger() -> logging.Logger:
    logger = logging.getLogger("admin_audit")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    path = current_app.config.get("ADMIN_LOG_PATH")
    handler = RotatingFileHandler(path, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
