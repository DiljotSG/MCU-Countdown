TMDB_BASE_URL = "api.themoviedb.org/3"
TMDB_BASE_IMG_URL = "image.tmdb.org/t/p/w500"
TMDB_LNG_DEFAULT = "en-CA"

TMDB_MCU_LIST = 140624
TMDB_STAR_WARS_LIST = 8563040
TMDB_DC_LIST = 8563041
TMDB_BATMAN_LIST = 8563043
TMDB_DILJOTS_LIST = 8630149

TMDB_DEFAULT_LIST = TMDB_MCU_LIST

NAMED_LISTS = {
    "mcu": {
        "list_id": TMDB_MCU_LIST,
        "name": "Marvel Cinematic Universe",
    },
    "star-wars": {
        "list_id": TMDB_STAR_WARS_LIST,
        "name": "Star Wars",
    },
    "dc": {
        "list_id": TMDB_DC_LIST,
        "name": "DC Universe",
    },
    "batman": {
        "list_id": TMDB_BATMAN_LIST,
        "name": "Matt Reeves' Batman Universe",
    },
    "diljots-list": {
        "list_id": TMDB_DILJOTS_LIST,
        "name": "Movies that I'm excited for - Diljot",
    }
}
