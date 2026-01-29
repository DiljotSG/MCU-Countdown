# Setup

This codebase uses **Python 3.11** (minimum 3.10). These setup instructions are for macOS using [Homebrew](https://brew.sh).
Installing these dependencies should be similar for other platforms with the appropriate package managers for that platform.

## Prerequisites

- Python 3.11 or higher
- A [TMDb API Key](https://developers.themoviedb.org/3) (requires free account)

## Python3 Installation

1. Install Python 3.11.

    ```shell
    brew install python@3.11
    ```

2. Verify installation:

    ```shell
    python3 --version
    # Should show Python 3.11.x or higher
    ```

## Local Development Setup

These steps are required for development.

1. Clone the repository.

    ```shell
    git clone https://github.com/DiljotSG/MCU-Countdown.git
    cd MCU-Countdown
    ```

2. Create a Python virtual environment.

    ```shell
    python3 -m venv venv
    ```

3. Activate the environment.

    ```shell
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```

4. Install Python dependencies.

    ```shell
    pip install -r requirements.txt
    pip install -r dev-requirements.txt  # For linting and formatting tools
    ```

5. Set up environment variables.

    You **must** have a TMDb API key. Get one from [TMDb](https://developers.themoviedb.org/3).

    ```shell
    export TMDB_API_KEY=your_api_key_here
    ```

    Optional environment variables:

    ```shell
    # Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    export LOG_LEVEL=DEBUG

    # Enable Flask debug mode for auto-reload
    export FLASK_DEBUG=true
    ```

6. Run the Flask application locally.

    ```shell
    python3 index.py
    ```

    The application will be available at `http://localhost:5000`

    Test the API:
    ```shell
    # Get next MCU production
    curl http://localhost:5000/api

    # Get next production from custom list
    curl "http://localhost:5000/api?list_id=140624"

    # View a TMDB list in your browser
    open https://www.themoviedb.org/list/140624
    ```

## Running Tests

1. Ensure you're in the virtual environment with dependencies installed.

2. Run all tests:

    ```shell
    python3 -m unittest discover tests
    ```

3. Run specific test file:

    ```shell
    python3 -m unittest tests.test_api -v
    python3 -m unittest tests.test_tmdb -v
    python3 -m unittest tests.test_oracle -v
    python3 -m unittest tests.test_production -v
    ```

## Deployment

### Docker

1. Build the Docker image.

    ```shell
    docker build -t mcu-countdown .
    ```

2. Run the container.

    ```shell
    docker run -p 5000:5000 -e TMDB_API_KEY=your_api_key mcu-countdown
    ```

### Docker Compose

1. Set your API key in an `.env` file or export it.

    ```shell
    export TMDB_API_KEY=your_api_key
    ```

2. Run with Docker Compose.

    ```shell
    docker compose up
    ```

## Configuration

### Cache Settings

The cache uses `cachetools.TTLCache` with a 1 hour TTL. Cache settings are defined in `src/services/tmdb.py`:

```python
_list_cache = TTLCache(maxsize=100, ttl=3600)
_last_page_cache = TTLCache(maxsize=100, ttl=3600)
```

### Response Cache Headers

HTTP cache headers are configured in `src/routes/root.py`. Default is 3600 seconds (1 hour).

```python
add_cache_headers(response, max_age=7200)  # 2 hours
```

## Troubleshooting

### Import Errors

If you get import errors, ensure you're in the project root directory and the virtual environment is activated.

### TMDB API Errors

- Verify your API key is set: `echo $TMDB_API_KEY`
- Test your API key at https://www.themoviedb.org/settings/api
- Check TMDB API status at https://status.themoviedb.org

### Cache Issues

During development, if you want to clear the cache:
1. Restart the Flask application
2. The in-memory cache will be cleared

## Development Tips

- Use `LOG_LEVEL=DEBUG` to see detailed request logging
- The cache significantly reduces TMDB API calls - you'll see faster responses on subsequent requests
- Test with custom TMDB lists to verify functionality
- All API responses include cache headers for CDN optimization
