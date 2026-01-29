# Routing

## Named Routes
Clean, memorable URLs for popular lists:

| Route | List | TMDB List ID |
|-------|------|--------------|
| `/` | Marvel Cinematic Universe | 140624 |
| `/star-wars` | Star Wars | 8563040 |
| `/dc` | DC Universe | 8563041 |
| `/batman` | Matt Reeves' Batman Universe | 8563043 |
| `/diljots-list` | Movies that I'm excited for - Diljot | 8630149 |

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
# Add a new list ID constant
TMDB_ANIME_LIST = 12345

# Add to NAMED_LISTS
NAMED_LISTS = {
    "mcu": {
        "list_id": TMDB_MCU_LIST,
        "name": "Marvel Cinematic Universe",
    },
    "star-wars": {
        "list_id": TMDB_STAR_WARS_LIST,
        "name": "Star Wars",
    },
    # Add your new route:
    "anime": {
        "list_id": TMDB_ANIME_LIST,
        "name": "Anime",
    },
}
```
