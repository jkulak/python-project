"""Logging configuration module using structlog."""

import logging
import os

import structlog
from dotenv import load_dotenv


def configure_logging():
    """Configure structured logging with JSON output and environment-based log level."""
    # Load environment variables
    load_dotenv()

    # Get log level from environment, default to INFO
    log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()

    # Convert string to logging level
    log_level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    log_level = log_level_map.get(log_level_str, logging.INFO)

    # Configure Python's standard logging
    logging.basicConfig(
        level=log_level,
        format="%(message)s",  # structlog will handle formatting
    )

    # Configure structlog
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def get_logger():
    """Get configured structlog logger."""
    return structlog.get_logger()


# Configure logging when module is imported
configure_logging()

# Export the logger instance
logger = get_logger()
