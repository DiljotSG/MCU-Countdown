import os
from typing import Optional

import requests

from src.common import is_valid_schema
from src.consts import (TMDB_BASE_IMG_URL, TMDB_BASE_URL, TMDB_LIST_SCHEMA,
                        TMDB_LNG_DEFAULT)


class TMDBService:
    def __init__(
        self,
        api_key: Optional[str] = None
    ):
        self.api_key: Optional[str] = os.getenv('TMDB_API_KEY', api_key)

    def send_request(
        self,
        rel_path: str,
        page_num: int = 1
    ) -> Optional[requests.Response]:
        if not self.api_key:
            return None
        return requests.get(
            "https://{}/{}".format(TMDB_BASE_URL, rel_path),
            params={
                "api_key": self.api_key,
                "language": TMDB_LNG_DEFAULT,
                "page": page_num
            },
            headers={
                "Content-Type": "application/json"
            }
        )

    def get_list(
        self,
        list_num: int,
        page_num: int = 1
    ) -> Optional[dict]:
        result = self.send_request("list/{}".format(list_num), page_num)
        if result and is_valid_schema(result.json(), TMDB_LIST_SCHEMA):
            return result.json()
        return None

    def give_poster_url(
        self,
        path_to_img: str
    ) -> str:
        return "https://{}{}".format(TMDB_BASE_IMG_URL, path_to_img)
