# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Main rules for Claude Code
Important: There is only docker intalled locally on this host. Always use Docker to run tests, install dependecies and manage the development environment.
Important: Always follow TDD (Test Driven Development). Before implementing functionality, always write tests.

1. **Understand the Code**: Analyze the code structure, dependencies, and functionality before making changes.
2. **Follow Project Conventions**: Adhere to existing coding styles, naming conventions, and project structure.
3. **Use Existing Tools**: Leverage existing tools for linting, formatting, and testing to maintain code quality.
4. **Document Changes**: Update documentation and comments to reflect any changes made to the codebase.
5. **Seek Feedback**: Encourage code reviews and discussions to improve code quality and share knowledge.
6. **Follow Best Practices**: Adhere to established best practices for coding, testing, and documentation including 12-factor app principles.
7. **Test Driven Development**: Write tests before implementing new features or fixing bugs to ensure code quality and functionality.

## Commands

### Development Environment
The project supports three development environments:

**Dev Container (Recommended)**:
- VS Code automatically detects `.devcontainer/devcontainer.json`
- Pre-configured with Python 3.12, Ruff formatter/linter, and pytest
- Uses `/opt/venv/bin/python` as interpreter

**Docker Compose**:
```bash
# Run application
docker compose up

# Run tests  
docker compose --profile testing up

# Interactive development shell
docker compose --profile development up -d
docker exec -it python-project-dev bash
```

**Local Development**:
```bash
pipenv install --dev
pipenv shell
```

### Testing
```bash
# In dev container or local environment
pytest -v --cov=src

# Run specific test file
pytest tests/test_main.py -v

# With Docker
docker compose --profile testing up
```

### Linting/Formatting
- Ruff is configured in dev container for auto-format on save
- Manual formatting: Use Ruff extension in VS Code or run `ruff format .`
- No separate lint command configured - relies on Ruff extension

### Running the Application
```bash
# In dev container or local
python src/main.py

# With Docker
docker compose up
```

## Architecture

### Project Structure
```
src/                 # All source code
├── __init__.py     
└── main.py          # Entry point with hello() function

tests/               # All test files  
├── __init__.py
└── test_main.py     # Tests for main.py
```

### Key Components
- **main.py**: Contains `hello()` function that prints greeting from environment variable or `.env` file
- **Environment Configuration**: Uses `python-dotenv` to load `.env` files, falls back to `GREETING_MESSAGE` env var or default "Hello, World!"
- **Testing**: Comprehensive pytest suite with mocking for environment variables and dotenv loading
- **Docker Multi-stage**: Optimized production builds with non-root user (uid 1000)

### Import Structure
- Tests use `sys.path` manipulation to import from `src/` directory
- Dev container sets `PYTHONPATH=/app/src` for clean imports
- Production Docker sets proper Python path in health check

### Dependencies
- **Runtime**: `python-dotenv` for environment variable management
- **Development**: `pytest`, `pytest-cov` for testing and coverage
- **Python Version**: 3.12 (enforced in Pipfile and Dockerfiles)

## Development Notes
- All environments use non-root user (appuser/uid 1000) for security
- Tests mock `load_dotenv()` to avoid side effects
- Docker volumes mount source code read-only in production profile
- Dev container includes Ruff, Copilot, and Python extensions pre-configured
