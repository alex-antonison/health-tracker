# Default recipe shows help
default:
    just --list

# Install dependencies using uv
install:
    echo "Installing dependencies with uv..."
    uv sync

# Install all dependencies including development tools
install-dev:
    echo "Installing all dependencies with uv..."
    uv sync --all-groups

# Run the health tracker script using uv
run:
    echo "Running health tracker script..."
    uv run health-tracker

# Run the health tracker script with verbose output
run-verbose:
    echo "Running health tracker script with verbose output..."
    uv run health-tracker --verbose

# Run unit tests using uv
test:
    echo "Running unit tests with uv..."
    uv sync --all-groups
    uv run python -m pytest tests/ -v

# Run sample data test
test-sample:
    echo "Running test with sample data..."
    uv run health-tracker --test-data

# Setup development environment
setup: install-dev
    echo "Development environment setup complete!"
    echo "Copy .envrc.template to .envrc and set the required environment variables."
    echo "This project uses uv for Python dependency management."
    echo "See AGENTS.md for development guidelines when working with AI agents."

# Clean build artifacts
clean:
    echo "Cleaning build artifacts..."
    rm -rf build/ dist/ *.egg-info/

# Show current status
status:
    echo "Checking project status..."
    just check-env
    
# Check environment variables
check-env:
    echo "Checking environment variables..."
    @if [ -z "$GOOGLE_CREDENTIAL_LOCATION" ]; then \
        echo "Warning: GOOGLE_CREDENTIAL_LOCATION is not set"; \
    else \
        echo "GOOGLE_CREDENTIAL_LOCATION is set to: $$GOOGLE_CREDENTIAL_LOCATION"; \
    fi