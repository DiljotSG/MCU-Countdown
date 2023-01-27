TMDB_BASE_URL = "api.themoviedb.org/3"
TMDB_BASE_IMG_URL = "image.tmdb.org/t/p/w500"
TMDB_MCU_LIST = 140624
TMDB_LNG_DEFAULT = "en-CA"
TMDB_LIST_SCHEMA = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "created_by": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "favorite_count": {
      "type": "number"
    },
    "id": {
      "type": "string"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "adult": {
            "type": "boolean"
          },
          "backdrop_path": {
            "type": [
               "string",
               "null"
            ]
          },
          "genre_ids": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "id": {
            "type": "number"
          },
          "media_type": {
            "type": "string"
          },
          "original_language": {
            "type": "string"
          },
          "original_title": {
            "type": "string"
          },
          "overview": {
            "type": "string"
          },
          "popularity": {
            "type": "number"
          },
          "poster_path": {
            "type": "string"
          },
          "release_date": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "video": {
            "type": "boolean"
          },
          "vote_average": {
            "type": "number"
          },
          "vote_count": {
            "type": "number"
          },
          "first_air_date": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "origin_country": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "original_name": {
            "type": "string"
          }
        }
      }
    },
    "item_count": {
      "type": "number"
    },
    "iso_639_1": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "poster_path": {}
  }
}
NOT_FOUND = 404
