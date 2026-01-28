# API

## Named Routes

For a better user experience, we provide clean URLs for popular lists:

- **`/`** - Marvel Cinematic Universe (default)
- **`/star-wars`** - Star Wars countdown
- **`/dc`** - DC Universe countdown
- **`/batman`** - Matt Reeves' Batman Universe countdown

These render HTML pages and can be used with the `?date=` parameter.

**Important Notes:**
- Named routes do NOT accept `list_id` query parameter - they always use their predefined list
- Named routes return HTML only - for JSON, use `/api?list_id=X`

## GET `/api`

Returns a JSON object detailing the next production from a TMDB list (defaults to MCU).

### Query Parameters

- `date` (optional): ISO formatted date (YYYY-MM-DD) to find the next production after this date. Defaults to today.
- `list_id` (optional): TMDB list ID to query. Defaults to the MCU list (140624). This allows you to use this API as a wrapper for any TMDB list!

### Response

```json
{
    "id": 12345,
    "days_until": 100,
    "overview": "Text Description",
    "poster_url": "https://image.tmdb.org/t/p/w500/path/to/poster.jpg",
    "release_date": "2020-05-01",
    "title": "MCU Film Title",
    "type": "TV Show | Movie",
    "following_production": {
        "id": 67890,
        "days_until": 200,
        "overview": "Next production description",
        "poster_url": "https://image.tmdb.org/t/p/w500/path/to/next_poster.jpg",
        "release_date": "2020-08-01",
        "title": "Next MCU Production",
        "type": "Movie"
    }
}
```

### Examples

#### Get next MCU production (default)
```
GET /api
```

#### Get next production after a specific date
```
GET /api?date=2020-11-01
```

#### Use a custom TMDB list
```
GET /api?list_id=12345
```

#### Try these custom lists for Star Wars and more
```
GET /api?list_id=8563040  # Star Wars
GET /api?list_id=8563041  # DC Universe
GET /api?list_id=8563043  # Matt Reeves' Batman Universe
```

#### Combine date and custom list
```
GET /api?date=2025-01-01&list_id=12345
```

## Validating TMDB Lists

To check if a TMDB list exists and see its contents, visit the list directly on TMDB:
```
https://www.themoviedb.org/list/YOUR_LIST_ID
```

For example, the MCU list: https://www.themoviedb.org/list/140624

## Caching

All endpoints include cache headers (`Cache-Control: public, max-age=3600`) to reduce lambda costs and improve performance. The API caches TMDB responses in-memory for 1 hour by default.

## Rate Limiting

This API is subject to TMDB's rate limits. Caching helps reduce the number of requests to TMDB.
