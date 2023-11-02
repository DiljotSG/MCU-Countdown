import os
from typing import Optional

import requests

from src.consts import (TMDB_BASE_IMG_URL, TMDB_BASE_URL, TMDB_LNG_DEFAULT)


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
        if result:
            return result.json()
        return None

    def get_last_page_list(
        self,
        list_num: int
    ) -> Optional[dict]:
        result = self.get_list(list_num)

        if result:
            current_page = result["page"]
            last_page = result["total_pages"]

            if current_page < last_page:
                result = self.get_list(list_num, last_page)

        return result

    def give_poster_url(
        self,
        path_to_img: str
    ) -> str:
        return "https://{}{}".format(TMDB_BASE_IMG_URL, path_to_img)
