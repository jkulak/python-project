import os
import sys
from unittest.mock import patch

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import hello


def test_hello_with_env_var(capsys, monkeypatch):
    """Test the hello function with custom environment variable."""
    monkeypatch.setenv("GREETING_MESSAGE", "Test greeting!")
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Test greeting!\n"


def test_hello_with_default(capsys, monkeypatch):
    """Test the hello function with default value when no env var is set."""
    monkeypatch.delenv("GREETING_MESSAGE", raising=False)
    with patch("main.load_dotenv"):
        hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_hello_with_dotenv_file(capsys, monkeypatch):
    """Test the hello function loads value from .env file correctly."""
    monkeypatch.delenv("GREETING_MESSAGE", raising=False)
    with patch("main.load_dotenv") as mock_load_dotenv:

        def side_effect():
            os.environ["GREETING_MESSAGE"] = "Hello from test .env file!"

        mock_load_dotenv.side_effect = side_effect
        hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello from test .env file!\n"


@patch("main.logger")
def test_hello_logs_environment_loading(mock_logger, capsys, monkeypatch):
    """Test that hello function logs environment variable loading."""
    monkeypatch.setenv("GREETING_MESSAGE", "Test greeting!")
    hello()
    mock_logger.info.assert_called()
    calls = mock_logger.info.call_args_list
    assert any(
        "environment variable loaded" in str(call) or "greeting_message" in str(call)
        for call in calls
    )


@patch("main.logger")
def test_hello_logs_default_fallback(mock_logger, capsys, monkeypatch):
    """Test that hello function logs when using default fallback."""
    monkeypatch.delenv("GREETING_MESSAGE", raising=False)
    with patch("main.load_dotenv"):
        hello()
    mock_logger.info.assert_called()
