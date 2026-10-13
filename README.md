# Health Tracker

A Python script to process health data from a Google Sheet and split it into separate tables for symptoms and measures.

This project was developed using an agentic development stack primarily for testing OpenRouter models:

### Agentic Stack
**Tools Used:**
1. **OpenRouter** for models
2. **Herdr** for multiplexer
3. **OpenCode** for running models

**Models Used:**
1. **Gemini 2.5 Pro** for planning and reasoning
2. **Qwen3 Coder 480B A35B** for doing development work

Note: This project is primarily for testing and demonstrating the capabilities of OpenRouter models rather than showcasing complex development work. The health tracker functionality itself is relatively straightforward but serves as a good example for evaluating AI-assisted development workflows.

### Python Environment Management

This project uses **uv** for Python dependency management. Please use uv commands for development:

- `uv sync` - Install dependencies
- `uv sync --all-groups` - Install all dependencies including development tools
- `uv run health-tracker` - Run the application
- `uv run python -m pytest tests/` - Run tests
- `uv add package-name` - Add new dependencies

## Setup

1. Ensure you have Python 3.13+ installed
2. Install [just](https://github.com/casey/just) command runner
3. Install dependencies using uv:
   ```
   just install
   ```

   Or manually with:
   ```
   uv sync
   ```

4. Set up environment variables:
   - Copy `.envrc.template` to `.envrc` and modify the variables:
     ```
     cp .envrc.template .envrc
     # Then edit .envrc to set the correct values
     ```
   - Set `GOOGLE_CREDENTIAL_LOCATION` to point to your Google Cloud credentials file
   - Set `SYMPTOM_GOOGLE_SHEET` to the name of your Google Sheet (defaults to "Symptom Tracker")

5. Ensure the Symptom Tracker Google Sheet exists with the following worksheets:
   - "Symptom Tracker" (input data)
   - "Data Symptoms Table" (output for symptoms)
   - "Data Measures Table" (output for measures)

## Usage

Run the script using:
```
just run
```

Or with verbose output:
```
just run-verbose
```

Alternatively, you can run with uv directly:
```
uv run health-tracker
```

Or directly with Python:
```
python -m src.health_tracker
```

The script will:
1. Read data from the "Symptom Tracker" worksheet
2. Split symptoms by the "|" delimiter into separate rows
3. Write the processed symptoms to "Data Symptoms Table"
4. Write the measures (Mobility and Notes) to "Data Measures Table"

Note: The output worksheets are cleared and fully replaced each time the script runs.

## Testing

To test the script functionality with sample data without connecting to Google Sheets:
```
just test
```

This will show how the data processing works with example data.

### Unit Tests

The project includes unit tests that can be run with pytest:
```
# Install dependencies including development tools
uv sync --all-groups

# Run the tests
uv run python -m pytest tests/ -v
```

These tests are also run automatically in CI/CD on pull requests.

### Sample Data Test

To see how the data processing works with example data:
```
just test-sample
```

Or run it directly:
```
uv run health-tracker --test-data
```

## Development

For development workflow commands, run:
```
just
```

This will show all available commands.

See [AGENTS.md](AGENTS.md) and [docs/development.md](docs/development.md) for guidelines about using uv and other development practices when working with AI agents.