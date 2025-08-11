import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

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
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
