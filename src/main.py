import os

from dotenv import load_dotenv

from utils.logger_config import logger


def hello():
    """Print a greeting message from environment variable."""
    logger.info("Loading environment configuration")
    load_dotenv()
    greeting = os.getenv("GREETING_MESSAGE", "Hello, World!")

    if greeting == "Hello, World!":
        logger.info("Using default greeting message", greeting_message=greeting)
    else:
        logger.info(
            "Environment variable loaded successfully", greeting_message=greeting
        )

    print(greeting)


if __name__ == "__main__":
    hello()
