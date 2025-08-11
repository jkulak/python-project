import os
import random
from datetime import datetime

from dotenv import load_dotenv


def hello():
    """Print a greeting message from environment variable."""
    load_dotenv()
    greeting = os.getenv("GREETING_MESSAGE", "Hello, World!")
    print(greeting)


def greet_user():
    """Ask for user's name and greet them with a random emoji."""
    emojis = ["🌟", "👋", "😊", "🎉", "🚀", "💫", "✨", "🌈", "🎈", "🔥"]

    name = input("What's your name? ").strip()

    if not name:
        name = "friend"

    emoji = random.choice(emojis)
    print(f"{emoji} Hello, {name}!")


def get_birth_year():
    """Ask for user's age and display the year they were born."""
    while True:
        try:
            age_input = input("What's your age? ")
            age = int(age_input)

            if age < 0:
                print("Please enter a valid age (cannot be negative).")
                continue

            current_year = datetime.now().year
            birth_year = current_year - age
            print(f"You were born in {birth_year}.")
            break

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    greet_user()
