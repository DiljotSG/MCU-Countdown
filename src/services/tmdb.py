import os
from typing import Optional

import requests

from src.consts import TMDB_BASE_IMG_URL, TMDB_BASE_URL, TMDB_LNG_DEFAULT
from src.logger import logger
from src.services.cache import get_cache


class TMDBService:
    def __init__(self, api_key: Optional[str] = None, cache_ttl: int = 3600):
        self.api_key: Optional[str] = os.getenv("TMDB_API_KEY", api_key)
        self.cache = get_cache()
        self.cache_ttl = cache_ttl  # Default: 1 hour

    def send_request(
        self, rel_path: str, page_num: int = 1
    ) -> Optional[requests.Response]:
        if not self.api_key:
            logger.error("TMDB API key not set!")
            return None

        url = "https://{}/{}".format(TMDB_BASE_URL, rel_path)

        try:
            response = requests.get(
                url,
                params={
                    "api_key": self.api_key,
                    "language": TMDB_LNG_DEFAULT,
                    "page": page_num,
                },
                headers={"Content-Type": "application/json"},
            )

            if response.status_code != 200:
                logger.warning(
                    f"TMDB API returned status {response.status_code}: {response.text}"
                )

            return response
        except Exception as e:
            logger.error(f"Error sending TMDB request: {str(e)}", exc_info=True)
            return None

    def get_list(self, list_num: int, page_num: int = 1) -> Optional[dict]:
        cache_key = f"tmdb_list_{list_num}_page_{page_num}"

        # Check cache first
        cached_result = self.cache.get(cache_key)
        if cached_result is not None:
            return cached_result

        # If not in cache, fetch from API
        result = self.send_request("list/{}".format(list_num), page_num)
        if result and result.status_code == 200:
            try:
                json_result = result.json()
                # Cache the result
                self.cache.set(cache_key, json_result, self.cache_ttl)
                return json_result
            except Exception as e:
                logger.error(f"Error parsing TMDB response: {str(e)}", exc_info=True)
                return None
        else:
            logger.warning(f"Failed to fetch list {list_num} from TMDB")
            return None

    def get_last_page_list(self, list_num: int) -> Optional[dict]:
        cache_key = f"tmdb_list_{list_num}_last_page"

        # Check cache first
        cached_result = self.cache.get(cache_key)
        if cached_result is not None:
            return cached_result

        result = self.get_list(list_num)

        if result:
            current_page = result["page"]
            last_page = result["total_pages"]

            if current_page < last_page:
                result = self.get_list(list_num, last_page)

            # Cache the last page result
            if result:
                self.cache.set(cache_key, result, self.cache_ttl)

        return result

    def give_poster_url(self, path_to_img: str) -> str:
        return "https://{}{}".format(TMDB_BASE_IMG_URL, path_to_img)
