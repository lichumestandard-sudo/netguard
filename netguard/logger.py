"""
NetGuard - Logging Module
Configures file + console logging for audit trails of scans and results.
"""

import logging
import os
from datetime import datetime


LOG_DIR = "logs"


def setup_logger(name: str = "netguard") -> logging.Logger:
    """
    Configure and return a logger that writes to both console and
    a timestamped log file under logs/.
    """
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    log_filename = os.path.join(LOG_DIR, f"netguard_{datetime.now().strftime('%Y%m%d')}.log")

    file_handler = logging.FileHandler(log_filename, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
