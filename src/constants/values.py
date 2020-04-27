TMDB_BASE_URL = "api.themoviedb.org/3"
TMDB_BASE_IMG_URL = "image.tmdb.org/t/p/w500"
TMDB_MCU_LIST = 140624
TMDB_LNG_DEFAULT = "en-US"
TMDB_LIST_SCHEMA = {
  "type": "object",
  "properties": {
    "created_by": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "favorite_count": {
      "type": "integer"
    },
    "id": {
      "type": "string"
    },
    "iso_639_1": {
      "type": "string"
    },
    "item_count": {
      "type": "integer"
    },
    "items": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "genre_ids": {
              "type": "array",
              "items": [
                {
                  "type": "integer"
                },
                {
                  "type": "integer"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "id": {
              "type": "integer"
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
              "type": "integer"
            }
          },
          "required": [
          ]
        }
      ]
    },
    "name": {
      "type": "string"
    },
    "poster_path": {
      "type": "null"
    }
  },
  "required": [
  ]
}
