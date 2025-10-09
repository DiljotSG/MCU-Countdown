# Testing

## Prerequisites

Install development dependencies:
```shell
pip install -r dev-requirements.txt
```

## Running Tests

### Unit Tests

Run all tests:
```shell
python3 -m unittest discover tests
```

Run a specific test file:
```shell
python3 -m unittest tests.test_api
python3 -m unittest tests.test_cache
python3 -m unittest tests.test_tmdb
python3 -m unittest tests.test_oracle
```

Run a specific test case:
```shell
python3 -m unittest tests.test_api.TestAPI.test_get_api
```

### Linting

Run flake8 to check code quality:
```shell
# Full lint (same as CI)
flake8 src/ tests/ --count --max-complexity=10 --max-line-length=127 --statistics

# Check for critical errors only
flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

### Code Formatting (Optional)

Format code with black:
```shell
black src/ tests/
```

Sort imports with isort:
```shell
isort src/ tests/
```

## Continuous Integration

All tests run automatically on every push via GitHub Actions:
- Unit tests with Python 3.11
- Flake8 linting
- Runs on all branches

See `.github/workflows/pythonapp.yml` for the CI configuration.
