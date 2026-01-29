import os
from typing import Optional

import httpx
from cachetools import TTLCache, cached

from src.consts import TMDB_BASE_IMG_URL, TMDB_BASE_URL, TMDB_LNG_DEFAULT
from src.logger import logger

_list_cache = TTLCache(maxsize=100, ttl=3600)
_last_page_cache = TTLCache(maxsize=100, ttl=3600)


class TMDBService:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key: Optional[str] = os.getenv("TMDB_API_KEY", api_key)
        self._client = httpx.Client(
            base_url=f"https://{TMDB_BASE_URL}",
            headers={"Content-Type": "application/json"},
            timeout=30.0,
        )

    def _get(self, path: str, page: int = 1) -> Optional[dict]:
        if not self.api_key:
            logger.error("TMDB API key not set!")
            return None

        try:
            response = self._client.get(
                path,
                params={
                    "api_key": self.api_key,
                    "language": TMDB_LNG_DEFAULT,
                    "page": page,
                },
            )

            if response.status_code != 200:
                logger.warning(
                    f"TMDB API returned status {response.status_code}: {response.text}"
                )
                return None

            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"HTTP error during TMDB request: {e}", exc_info=True)
            return None
        except Exception as e:
            logger.error(f"Error during TMDB request: {e}", exc_info=True)
            return None

    @cached(_list_cache)
    def get_list(self, list_num: int, page_num: int = 1) -> Optional[dict]:
        return self._get(f"/list/{list_num}", page_num)

    @cached(_last_page_cache)
    def get_last_page_list(self, list_num: int) -> Optional[dict]:
        result = self.get_list(list_num)

        if not result:
            return None

        current_page = result.get("page", 1)
        last_page = result.get("total_pages", 1)

        if current_page < last_page:
            result = self.get_list(list_num, last_page)

        return result

    def give_poster_url(self, path_to_img: str) -> str:
        return f"https://{TMDB_BASE_IMG_URL}{path_to_img}"
