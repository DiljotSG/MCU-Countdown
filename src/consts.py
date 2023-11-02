TMDB_BASE_URL = "api.themoviedb.org/3"
TMDB_BASE_IMG_URL = "image.tmdb.org/t/p/w500"
TMDB_MCU_LIST = 140624
TMDB_LNG_DEFAULT = "en-CA"
TMDB_LIST_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
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
      "type": "integer"
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
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
                },
                {
                  "type": "integer"
                }
              ]
            },
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        },
        {
          "type": "object",
          "properties": {
            "adult": {
              "type": "boolean"
            },
            "backdrop_path": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "title": {
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
            "poster_path": {
              "type": "string"
            },
            "media_type": {
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
            "popularity": {
              "type": "number"
            },
            "release_date": {
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
            "adult",
            "backdrop_path",
            "id",
            "title",
            "original_language",
            "original_title",
            "overview",
            "poster_path",
            "media_type",
            "genre_ids",
            "popularity",
            "release_date",
            "video",
            "vote_average",
            "vote_count"
          ]
        }
      ]
    },
    "name": {
      "type": "string"
    },
    "page": {
      "type": "integer"
    },
    "poster_path": {
      "type": "null"
    },
    "total_pages": {
      "type": "integer"
    },
    "total_results": {
      "type": "integer"
    }
  },
  "required": [
    "created_by",
    "description",
    "favorite_count",
    "id",
    "iso_639_1",
    "item_count",
    "items",
    "name",
    "page",
    "poster_path",
    "total_pages",
    "total_results"
  ]
}
NOT_FOUND = 404
