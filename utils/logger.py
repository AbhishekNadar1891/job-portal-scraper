import logging
import os

from config import OUTPUT_DIR, LOG_FILE


def get_logger(name):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        os.path.join(OUTPUT_DIR, LOG_FILE),
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger