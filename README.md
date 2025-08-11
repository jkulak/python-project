# Python Project

A modern Python project scaffold with pipenv dependency management, pytest testing, and Docker containerization.

## Project Overview

This project demonstrates a simple Python application with:
- A `hello()` function that prints a greeting
- Comprehensive test coverage using pytest
- **Organized structure**: Separate `src/` and `tests/` directories
- Modern dependency management with pipenv
- Dockerized development and production environments
- Multi-stage Docker builds for optimization
- **Scalable architecture**: Ready for dozens of source files and tests

## Quick Start

### Using Docker (Recommended)

1. **Run the application**:
   ```bash
   docker compose up
   ```

2. **Run tests**:
   ```bash
   docker compose --profile testing up
   ```

3. **Interactive development**:
   ```bash
   docker compose --profile development up
   ```

### Local Development

1. **Install dependencies**:
   ```bash
   pip install pipenv
   pipenv install --dev
   ```

2. **Activate virtual environment**:
   ```bash
   pipenv shell
   ```

3. **Run the application**:
   ```bash
   python src/main.py
   ```

4. **Run tests**:
   ```bash
   pytest
   ```

## Development Workflow

### Docker Development

The project includes three Docker Compose profiles for different development needs:

#### 1. Running the Application
```bash
docker compose up
```
- Runs the main application
- Mounts current directory for live code changes
- Uses non-root user for security

#### 2. Running Tests
```bash
docker compose --profile testing up
```
- Executes all tests with verbose output
- Mounts current directory to test latest changes
- Automatically exits after test completion

#### 3. Interactive Development

**Option 1 (Detached + Exec)**:
```bash
docker compose --profile development up -d
docker exec -it python-project-dev bash
```

**Option 2 (Direct Run)**:
```bash
docker compose --profile development run --rm dev
```

Both options provide:
- Interactive bash shell inside the container
- Full access to the containerized environment  
- All dependencies pre-installed and ready to use

**Note**: Running `docker compose --profile development up` (without `-d`) only shows container logs and doesn't provide shell access. Use one of the two options above for interactive development.

#### Useful Docker Commands
```bash
# Build the image manually
docker build -t python-project .

# Run a one-off command
docker compose run --rm app python main.py

# Run tests in a one-off container
docker compose run --rm test

# Stop and remove all containers
docker compose down
```

### Local Development (Pipenv)

If you prefer local development without Docker:

```bash
# Install dependencies
pipenv install --dev

# Activate virtual environment
pipenv shell

# Run application
python src/main.py

# Run tests
pytest -v

# Run specific test file
pytest tests/test_main.py

# Install new dependency
pipenv install <package_name>

# Install new dev dependency
pipenv install --dev <package_name>
```

## Testing

The project uses pytest for testing with the following setup:

- **Test directory**: `tests/` - Contains all test files
- **Test files**: `tests/test_main.py` - Tests for main.py functions
- **Configuration**: `pytest.ini` - Configured to run tests from tests/ directory
- **Test runner**: pytest with verbose output and short traceback
- **Import structure**: Uses PYTHONPATH for clean imports from src/ directory

### Running Tests

**With Docker**:
```bash
# Run all tests
docker compose --profile testing up

# Run tests interactively
docker compose run --rm test

# Run tests with custom options
docker compose run --rm app pytest -v -s
```

**Locally**:
```bash
# With pipenv
pipenv run pytest

# In activated virtual environment
pytest

# With specific options
pytest -v --tb=short
```

## Project Structure

```
.
├── src/                 # Source code directory
│   ├── __init__.py      # Package initialization  
│   └── main.py          # Main application code
├── tests/               # Test files directory
│   ├── __init__.py      # Package initialization
│   └── test_main.py     # Test file for main.py
├── Pipfile              # Pipenv dependencies
├── Pipfile.lock         # Locked dependency versions
├── pytest.ini          # Pytest configuration
├── Dockerfile           # Multi-stage Docker build
├── compose.yml          # Docker Compose configuration
├── .dockerignore        # Docker build exclusions
├── CLAUDE.md            # Claude Code guidance
└── README.md            # This file
```

### Directory Structure Benefits

- **`src/`**: Clean separation of source code from configuration files
- **`tests/`**: Dedicated directory for all test files
- **Scalability**: Easy to organize when you have dozens of modules and tests
- **Clear imports**: PYTHONPATH configured for clean `from main import hello`
- **Docker optimization**: Selective mounting of directories in containers

## Docker Best Practices

This project implements several Docker best practices:

- **Multi-stage builds**: Separate builder and runtime stages for smaller images
- **Security**: Non-root user execution (uid 1000)
- **Layer caching**: Dependencies installed before code copy
- **Minimal base image**: Uses `python:3.12-slim`
- **Health checks**: Container monitoring and status reporting
- **Environment optimization**: Proper Python environment variables

## Requirements

- **Docker & Docker Compose**: For containerized development
- **Python 3.12+**: For local development
- **pipenv**: For dependency management (local development)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `docker compose --profile testing up`
5. Submit a pull request

## License

This project is a development scaffold and template.