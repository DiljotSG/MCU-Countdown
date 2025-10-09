from datetime import MAXYEAR, date
from typing import List, Optional, Tuple

from src.consts import TMDB_MCU_LIST
from src.exceptions import ListNotFoundError, NoUpcomingProductionsError
from src.services.tmdb import TMDBService


class Oracle:
    def __init__(self):
        self.tmdb: TMDBService = TMDBService()
        self.max_date = "{}-01-01".format(MAXYEAR)

    def _fetch_production_list(self, tmdb_list_id: Optional[int] = None) -> List[dict]:
        list_id = tmdb_list_id if tmdb_list_id else TMDB_MCU_LIST
        response = self.tmdb.get_last_page_list(list_id)

        if not response:
            raise ListNotFoundError(list_id)

        production_list = response.get("items", [])

        if not production_list:
            raise ListNotFoundError(list_id, f"List {list_id} exists but has no items")

        return production_list

    def _get_production_release_date(self, production: dict) -> str:
        return production.get("release_date", production.get("first_air_date", self.max_date))

    def _find_next_after_date(
        self, productions: List[dict],
        desired_date: str,
        list_id: Optional[int] = None
    ) -> Optional[int]:
        try:
            index = next(
                i
                for i, prod in enumerate(productions)
                if self._get_production_release_date(prod) > desired_date
            )
            return index
        except StopIteration:
            raise NoUpcomingProductionsError(list_id=list_id, desired_date=desired_date)

    def _get_following_production(
        self,
        productions: List[dict],
        current_index: int,
    ) -> Optional[dict]:
        if current_index + 1 < len(productions):
            return productions[current_index + 1]
        return None

    def get_next_production(
        self,
        production_list: Optional[List[dict]] = None,
        desired_date: Optional[str] = None,
        tmdb_list_id: Optional[int] = None,
    ) -> Optional[Tuple[dict, Optional[dict]]]:
        # Fetch production list if not provided
        if not production_list:
            production_list = self._fetch_production_list(tmdb_list_id)

        # Use today's date if not specified
        if not desired_date:
            desired_date = date.today().isoformat()

        # Determine the actual list_id being used
        actual_list_id = tmdb_list_id if tmdb_list_id else TMDB_MCU_LIST

        # Find the next production after the desired date
        index = self._find_next_after_date(production_list, desired_date, actual_list_id)

        if index is None:
            return None

        next_production = production_list[index]

        # Get the following production if available
        following_production = self._get_following_production(production_list, index)

        return next_production, following_production

    def format_output_dict(self, tmdb_item: dict) -> dict:
        result: dict = {}
        release_date = tmdb_item.get(
            "release_date", tmdb_item.get("first_air_date", None)
        )
        media_type = tmdb_item.get("media_type", "")

        if not release_date:
            return {}

        days_until = date.fromisoformat(release_date) - date.today()

        result["release_date"] = release_date
        result["title"] = tmdb_item.get(
            "original_title", tmdb_item.get("original_name", "")
        )
        result["poster_url"] = self.tmdb.give_poster_url(
            tmdb_item.get("poster_path", "")
        )
        result["overview"] = tmdb_item.get("overview", "")
        result["days_until"] = int(days_until.days)
        result["type"] = "TV Show" if media_type == "tv" else "Movie"
        result["id"] = tmdb_item.get("id", -1)
        return result

    def get_next_mcu_production(
        self,
        desired_date: Optional[str] = None,
        tmdb_list_id: Optional[int] = None,
    ) -> dict:
        result: dict = {}

        items = self.get_next_production(
            desired_date=desired_date,
            tmdb_list_id=tmdb_list_id
        )

        if not items:
            return result

        next_production, following_production = items

        if next_production:
            result = self.format_output_dict(next_production)

            if following_production:
                result["following_production"] = self.format_output_dict(
                    following_production
                )

        return result
