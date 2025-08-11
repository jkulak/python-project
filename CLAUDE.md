# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a modern Python project using pipenv for dependency management and pytest for testing. The project contains a simple greeting function with corresponding tests. It's fully containerized with Docker using multi-stage builds for optimization.

## Development Setup

### Local Development (with pipenv)
1. Install pipenv if not already installed: `pip install pipenv`
2. Install dependencies: `pipenv install --dev`
3. Activate virtual environment: `pipenv shell`

### Docker Development
1. Build the Docker image: `docker build -t python-project .`
2. Run with Docker Compose: `docker compose up`

## Common Development Commands

### Dependency Management
- `pipenv install <package>` - Install a runtime dependency
- `pipenv install --dev <package>` - Install a development dependency
- `pipenv install` - Install all dependencies from Pipfile
- `pipenv shell` - Activate the virtual environment
- `pipenv run <command>` - Run a command within the virtual environment

### Testing
- `pipenv run pytest` - Run all tests
- `pipenv run pytest -v` - Run tests with verbose output
- `pipenv run pytest tests/test_main.py` - Run specific test file
- `pytest tests/` - Run all tests in tests directory (when in pipenv shell)

### Code Quality
- Linting and formatting handled by ruff VS Code extension (charliermarsh.ruff)
- Configured to format on save and fix issues automatically
- Import sorting and code fixes applied on save

### Running the Application
- `pipenv run python src/main.py` - Run the main application
- `python src/main.py` - Run main application (when in pipenv shell)

### Docker Commands
- `docker build -t python-project .` - Build the Docker image
- `docker run python-project` - Run the application in a container
- `docker compose up` - Run the application using Docker Compose
- `docker compose --profile testing up` - Run tests in a container
- `docker compose --profile development up` - Start interactive development container
- `docker compose down` - Stop and remove containers

## Project Structure

- `src/` - Source code directory
  - `main.py` - Main application code with hello() function
  - `__init__.py` - Package initialization
- `tests/` - Test files directory
  - `test_main.py` - Test file for main.py functions
  - `__init__.py` - Package initialization
- `Pipfile` - Pipenv dependency specification
- `pytest.ini` - Pytest configuration (configured for tests/ directory)
- `Dockerfile` - Multi-stage Docker build configuration
- `compose.yml` - Docker Compose configuration with profiles
- `.dockerignore` - Files excluded from Docker build context
- `README.md` - Project documentation

## Architecture

Organized Python project with separate source and test directories:
- **Source code**: Located in `src/` directory for clean organization
- **Tests**: Located in `tests/` directory with PYTHONPATH configured for imports  
- `hello()` function in src/main.py that prints a greeting
- Test coverage using pytest with capsys fixture for output testing
- Modern Python development workflow using pipenv for dependency isolation
- Containerized with Docker using multi-stage builds for optimization
- Non-root user execution for security
- Health checks for container monitoring
- **Scalable structure**: Ready for dozens of source files and test files

## Docker Best Practices Implemented

- **Multi-stage builds**: Separate builder and runtime stages for smaller final image
- **Layer caching**: Dependencies installed before code copy for better cache utilization
- **Security**: Non-root user execution (uid 1000)
- **Optimization**: Minimal slim base image, .dockerignore to exclude unnecessary files
- **Development workflow**: Compose profiles for different environments (app, test, dev)
- **Environment variables**: Proper Python settings (PYTHONDONTWRITEBYTECODE, PYTHONUNBUFFERED)