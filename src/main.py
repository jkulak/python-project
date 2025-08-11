import os
from dotenv import load_dotenv


def hello():
    """Print a greeting message from environment variable."""
    load_dotenv()
    greeting = os.getenv("GREETING_MESSAGE", "Hello, World!")
    print(greeting)


if __name__ == "__main__":
    hello()