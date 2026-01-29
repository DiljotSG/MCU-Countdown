# MCU-Countdown

When is the next MCU film? A simple but powerful API wrapper for TMDB lists.

## Screenshot

<img width="1137" height="1028" alt="image" src="https://github.com/user-attachments/assets/5271cec4-28ab-47be-9719-207f338ab51e" />

**Production API Endpoint:** <https://www.whenisthenextmcufilm.com>

## Running with Docker

The app can be run and self-hosted using Docker Compose.

Create a [`docker-compose.yml`](docker-compose.yml).

### Docker Compose

```bash
# Set your TMDB API key or set it in a .env file
export TMDB_API_KEY=your_api_key_here

# Run the app
docker compose up -d
```

The app will be available at `http://localhost:5000`


### Building Image with Docker

```bash
# Build the image
docker build -t mcu-countdown .

# Run the container
docker run -p 5000:5000 -e TMDB_API_KEY=your_api_key_here mcu-countdown
```

## Quick Start

### Default MCU Usage

```bash
# Get the next MCU production
curl https://www.whenisthenextmcufilm.com/api
```

### Named Routes for Alternative collections

- Star Wars: https://www.whenisthenextmcufilm.com/star-wars
- DC Universe: https://www.whenisthenextmcufilm.com/dc
- Matt Reeves' Batman Universe: https://www.whenisthenextmcufilm.com/batman

### Custom List Usage

**Note**: You can view any TMDB list at: https://www.themoviedb.org/list/YOUR_LIST_ID

```bash
# Use any TMDB list by ID
curl "https://www.whenisthenextmcufilm.com/api?list_id=YOUR_LIST_ID"
```

### With Date Parameter

```bash
# Get the next production after a specific date
curl "https://www.whenisthenextmcufilm.com/api?date=2025-01-01"

# Combine with custom list
curl "https://www.whenisthenextmcufilm.com/api?date=2025-01-01&list_id=YOUR_LIST_ID"
```

## Documentation

* [API Reference](docs/API.md) - Complete API documentation
* [Setup Guide](docs/SETUP.md) - Local development setup
* [Testing](docs/TESTING.md) - Running tests
* [Routing](docs/ROUTING.md) - Routing information

## Example Response

```json
{
  "id": 533535,
  "title": "Deadpool & Wolverine",
  "type": "Movie",
  "release_date": "2024-07-24",
  "days_until": 289,
  "overview": "A listless Wade Wilson toils away in civilian life...",
  "poster_url": "https://image.tmdb.org/t/p/w500/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg",
  "following_production": {
    "id": 912649,
    "title": "Venom: The Last Dance",
    "type": "Movie",
    "release_date": "2024-10-22",
    "days_until": 379,
    "overview": "Eddie and Venom are on the run...",
    "poster_url": "https://image.tmdb.org/t/p/w500/..."
  }
}
```

## Contributing

Contributions are welcome! Please feel free to open a PR with your changes!

## License

See [LICENSE](LICENSE) file for details.

## Credits

Special thanks to TMDB for their excellent API.
