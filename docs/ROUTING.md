# Routing

## Named Routes
Clean, memorable URLs for popular lists:

| Route | List | TMDB List ID |
|-------|------|--------------|
| `/` | Marvel Cinematic Universe | 140624 |
| `/star-wars` | Star Wars | 8563040 |
| `/dc` | DC Universe | 8563041 |
| `/batman` | Matt Reeves Batman Universe | 8563043 |

## Custom Lists via Query Parameter

For any TMDB list not in the named routes:

| Route | Description |
|-------|-------------|
| `/?list_id=X` | HTML page for custom list X |
| `/api?list_id=X` | JSON API for custom list X |

## API Endpoint

JSON responses for any list:

| Route | Description |
|-------|-------------|
| `/api` | JSON for MCU (default) |
| `/api?list_id=X` | JSON for custom list X |
| `/api?date=Y` | JSON for MCU after date Y |
| `/api?date=Y&list_id=X` | JSON for list X after date Y |


## Adding New Named Routes

To add a new named route, edit `src/consts.py`:

```python
NAMED_LISTS = {
    "star-wars": {
        "list_id": 8563040,
        "name": "Star Wars",
    },
    "dc": {
        "list_id": 8563041,
        "name": "DC Universe",
    },
    "batman": {
        "list_id": 8563043,
        "name": "Matt Reeves Batman Universe",
    },
    # Add your new route here:
    "anime": {
        "list_id": YOUR_LIST_ID,
        "name": "Anime",
    }
}
```
