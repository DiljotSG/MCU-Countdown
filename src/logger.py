import logging
import os
import sys


def setup_logger(name: str = "mcu-countdown") -> logging.Logger:
    logger = logging.getLogger(name)

    # Get log level from environment or default to INFO
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logger.setLevel(getattr(logging, log_level, logging.INFO))

    # Only add handler if none exist (prevents duplicate logs)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logger.level)

        # Format for AWS Lambda and local development
        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger


# Create a default logger instance
logger = setup_logger()
