# Multi-stage Dockerfile for Python project with pipenv

# Builder stage - install dependencies
FROM python:3.13.7-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIPENV_VENV_IN_PROJECT=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Create and set working directory
WORKDIR /app

# Copy dependency files
COPY Pipfile Pipfile.lock* ./

# Install dependencies
RUN pipenv install --deploy --dev

# Runtime stage - minimal image
FROM python:3.13.7-slim AS runtime

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH" \
    GREETING_MESSAGE="Hello from Docker!"

# Create non-root user
RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

# Set working directory
WORKDIR /app

# Copy virtual environment from builder stage to /opt/venv
COPY --from=builder /app/.venv /opt/venv

# Copy application code
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD /opt/venv/bin/python -c "import sys; sys.path.insert(0, 'src'); import main; print('OK')" || exit 1

# Default command
CMD ["/opt/venv/bin/python", "src/main.py"]
