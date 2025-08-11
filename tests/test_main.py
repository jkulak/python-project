import os
import sys
from unittest.mock import patch

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import hello, greet_user, get_birth_year


def test_hello_with_env_var(capsys, monkeypatch):
    """Test the hello function with custom environment variable."""
    monkeypatch.setenv("GREETING_MESSAGE", "Test greeting!")
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Test greeting!\n"


def test_hello_with_default(capsys, monkeypatch):
    """Test the hello function with default value when no env var is set."""
    monkeypatch.delenv("GREETING_MESSAGE", raising=False)
    with patch('main.load_dotenv'):
        hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_hello_with_dotenv_file(capsys, monkeypatch):
    """Test the hello function loads value from .env file correctly."""
    monkeypatch.delenv("GREETING_MESSAGE", raising=False)
    with patch('main.load_dotenv') as mock_load_dotenv:
        def side_effect():
            os.environ["GREETING_MESSAGE"] = "Hello from test .env file!"
        mock_load_dotenv.side_effect = side_effect
        hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello from test .env file!\n"


def test_greet_user_normal_input(capsys):
    """Test greet_user with normal name input."""
    with patch('main.input', return_value='Alice'), \
         patch('main.random.choice', return_value='🌟'):
        greet_user()
    captured = capsys.readouterr()
    assert captured.out == "🌟 Hello, Alice!\n"


def test_greet_user_empty_input(capsys):
    """Test greet_user with empty string input."""
    with patch('main.input', return_value=''), \
         patch('main.random.choice', return_value='👋'):
        greet_user()
    captured = capsys.readouterr()
    assert captured.out == "👋 Hello, friend!\n"


def test_greet_user_whitespace_input(capsys):
    """Test greet_user with whitespace-only input."""
    with patch('main.input', return_value='   '), \
         patch('main.random.choice', return_value='😊'):
        greet_user()
    captured = capsys.readouterr()
    assert captured.out == "😊 Hello, friend!\n"


def test_greet_user_long_name(capsys):
    """Test greet_user with very long name input."""
    long_name = 'A' * 100
    with patch('main.input', return_value=long_name), \
         patch('main.random.choice', return_value='🎉'):
        greet_user()
    captured = capsys.readouterr()
    assert captured.out == f"🎉 Hello, {long_name}!\n"


def test_greet_user_emoji_randomness(capsys):
    """Test that greet_user uses random.choice for emoji selection."""
    with patch('main.input', return_value='Bob'), \
         patch('main.random.choice', return_value='🚀') as mock_choice:
        greet_user()
    mock_choice.assert_called_once()
    captured = capsys.readouterr()
    assert captured.out == "🚀 Hello, Bob!\n"


def test_greet_user_input_prompt():
    """Test that greet_user prompts for user input."""
    with patch('main.input', return_value='Charlie') as mock_input, \
         patch('main.random.choice', return_value='💫'):
        greet_user()
    mock_input.assert_called_once_with("What's your name? ")


def test_greet_user_strips_whitespace(capsys):
    """Test that greet_user strips whitespace from input."""
    with patch('main.input', return_value='  David  '), \
         patch('main.random.choice', return_value='✨'):
        greet_user()
    captured = capsys.readouterr()
    assert captured.out == "✨ Hello, David!\n"


def test_get_birth_year_valid_age(capsys):
    """Test get_birth_year with valid age input."""
    with patch('main.input', return_value='25'):
        get_birth_year()
    captured = capsys.readouterr()
    current_year = 2025
    expected_birth_year = current_year - 25
    assert f"You were born in {expected_birth_year}" in captured.out


def test_get_birth_year_zero_age(capsys):
    """Test get_birth_year with zero age."""
    with patch('main.input', return_value='0'):
        get_birth_year()
    captured = capsys.readouterr()
    current_year = 2025
    expected_birth_year = current_year - 0
    assert f"You were born in {expected_birth_year}" in captured.out


def test_get_birth_year_invalid_input_then_valid(capsys):
    """Test get_birth_year with invalid input followed by valid input."""
    with patch('main.input', side_effect=['abc', '30']):
        get_birth_year()
    captured = capsys.readouterr()
    assert "Please enter a valid number" in captured.out
    current_year = 2025
    expected_birth_year = current_year - 30
    assert f"You were born in {expected_birth_year}" in captured.out


def test_get_birth_year_negative_age_then_valid(capsys):
    """Test get_birth_year with negative age followed by valid input."""
    with patch('main.input', side_effect=['-5', '22']):
        get_birth_year()
    captured = capsys.readouterr()
    assert "Please enter a valid age" in captured.out
    current_year = 2025
    expected_birth_year = current_year - 22
    assert f"You were born in {expected_birth_year}" in captured.out


def test_get_birth_year_prompt_message():
    """Test that get_birth_year prompts with correct message."""
    with patch('main.input', return_value='25') as mock_input:
        get_birth_year()
    mock_input.assert_called_with("What's your age? ")
