# API

## GET `/api`

Returns a JSON object detailing the next MCU production.

Example
```json
{
    "days_until": 100,
    "overview": "Text Description",
    "poster_url": "https://image.tmdb.org/t/p/w500/path/to/poster.jpg",
    "release_date": "2020-05-01",
    "title": "MCU Film Title",
    "type": "TV Show | Movie",
    "following_production": {...}
}
```

Takes in an optional date parameter. If this date isn't passed, we use today's date by default.

Example: **GET `/api?date=2020-11-01`**.
*Note*: must be an ISO formatted date.
