# MCU-Countdown

When is the next MCU film? A simple but powerful API wrapper for TMDB lists.

## What's New

This API has been significantly improved with:
- The ability to use any custom TMDB list, not just the MCU. You can track Star Wars, DC, The Batman, or other custom collections!
- In-memory caching with TTL support.

**Production API Endpoint:** <https://www.whenisthenextmcufilm.com>
**Development API Endpoint:** <https://dev.whenisthenextmcufilm.com>

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

## Technology Stack

- **Framework**: Flask 3.0
- **Deployment**: AWS Lambda (Serverless)
- **Runtime**: Python 3.11
- **Caching**: In-memory with TTL
- **API**: TMDB (The Movie Database)

## Contributing

Contributions are welcome! Please feel free to open a PR with your changes!

## License

See [LICENSE](LICENSE) file for details.

## Credits

Special thanks to TMDB for their excellent API.
