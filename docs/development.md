# Agent Development Guidelines

This project uses specific tools and practices that agents should be aware of to maintain consistency and avoid conflicts.

## Python Environment Management

This project uses **uv** for Python dependency management. Agents should use uv commands rather than pip:

### Key Commands
- `uv sync` - Install production dependencies
- `uv sync --all-groups` - Install all dependencies (including development tools)
- `uv run health-tracker` - Run the application
- `uv run python -m pytest tests/` - Run tests
- `uv add package-name` - Add new dependencies

### Why uv?
1. Faster dependency resolution than pip
2. Consistent environment across all developers
3. Better integration with the project's tooling
4. Prevents conflicts with existing pip installations

## Project Structure
```
health-tracker/
├── .github/workflows/ # CI/CD workflows
├── docs/               # Documentation
├── llm/                # LLM-related files
├── src/                 # Source code
├── tests/              # Unit tests
├── Justfile            # Development commands
├── pyproject.toml      # Project metadata and dependencies
└── uv.lock             # Locked dependencies
```

## Development Workflow
1. Use `just setup` for initial setup (installs dependencies with uv)
2. Use `just test` to run tests (uses uv under the hood)
3. Use `just run` to execute the application
4. Always use `uv add` instead of `pip install` for new dependencies

## Continuous Integration
Tests run automatically on pull requests using GitHub Actions, which also uses uv for dependency management.

### Pull Request Guidelines
Always create pull requests as drafts initially:
1. Draft PRs prevent premature CI runs and notifications
2. Convert to ready for review when work is complete
3. This saves CI resources and reduces notification noise

### Pull Request Guidelines
Always create pull requests as drafts initially:
1. Draft PRs prevent premature CI runs and notifications
2. Convert to ready for review when work is complete
3. This saves CI resources and reduces notification noise