import os
import requests
from src.common import is_valid_schema
from src.constants.values import TMDB_BASE_URL
from src.constants.values import TMDB_LNG_DEFAULT
from src.constants.values import TMDB_LIST_SCHEMA
from src.constants.values import TMDB_BASE_IMG_URL

from typing import Optional


class TMDBService:
    def __init__(
        self,
        api_key: Optional[str] = None
    ):
        self.api_key: Optional[str] = os.getenv('TMDB_API_KEY', api_key)

    def __send_request(self, rel_path: str) -> requests.Response:
        if self.api_key:
            return requests.get(
                "https://{}/{}".format(TMDB_BASE_URL, rel_path),
                params={
                    "api_key": self.api_key,
                    "language": TMDB_LNG_DEFAULT
                },
                headers={
                    "Content-Type": "application/json"
                }
            )

    def get_list(self, list_num: int) -> dict:
        result = self.__send_request("list/{}".format(list_num)).json()
        is_valid_schema(result, TMDB_LIST_SCHEMA)
        return result["items"]

    def get_poster_url(self, path: str) -> str:
        return "https://{}/{}".format(TMDB_BASE_IMG_URL, path)
