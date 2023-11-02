from datetime import MAXYEAR, date
from typing import List, Optional

from src.consts import TMDB_MCU_LIST
from src.services.tmdb import TMDBService


class Oracle:
    def __init__(self):
        self.tmdb: TMDBService = TMDBService()
        self.max_date = "{}-01-01".format(MAXYEAR)

    def get_next_production(
        self,
        production_list: Optional[dict] = None,
        desired_date: Optional[str] = None
    ) -> Optional[List]:
        response = None

        if not production_list:
            response = self.tmdb.get_list(TMDB_MCU_LIST)
            production_list = response["items"]
            current_page = response["page"]
            total_num_pages = response["total_pages"]
            
            if current_page < total_num_pages:
                response = self.tmdb.get_list(TMDB_MCU_LIST, total_num_pages)
                production_list = response["items"]


        if production_list:
            if not desired_date:
                desired_date = date.today().isoformat()

            try:
                # Find the first film with a release date larger than the current date
                index: int = next(
                    i for i, v in enumerate(production_list)
                    if v.get("release_date", v.get("first_air_date", self.max_date)) > desired_date
                )
                if index is not None:
                    next_production = production_list[index]

                    following_production = None
                    if index + 1 < len(production_list):
                        following_production = production_list[index + 1]

                    return [next_production, following_production]
            except StopIteration:
                pass

        return None

    def format_output_dict(self, tmdb_item: dict) -> dict:
        result: dict = {}
        release_date = tmdb_item.get("release_date", tmdb_item.get("first_air_date", None))
        media_type = tmdb_item.get("media_type", "")

        if not release_date:
            return {}

        days_until = date.fromisoformat(release_date) - date.today()

        result["release_date"] = release_date
        result["title"] = tmdb_item.get("original_title", tmdb_item.get("original_name", ""))
        result["poster_url"] = self.tmdb.give_poster_url(tmdb_item.get("poster_path", ""))
        result["overview"] = tmdb_item.get("overview", "")
        result["days_until"] = int(days_until.days)
        result["type"] = "TV Show" if media_type == "tv" else "Movie"
        result["id"] = tmdb_item.get("id", -1)
        return result

    def get_next_mcu_production(
        self,
        desired_date: Optional[str] = None
    ) -> dict:
        result: dict = {}
        items: Optional[List[dict]] = self.get_next_production(
            desired_date=desired_date
        )

        next_production: Optional[dict] = None
        following_production: Optional[dict] = None
        if items:
            next_production = items[0]
            if len(items) > 1:
                following_production = items[1]

        if next_production:
            result = self.format_output_dict(next_production)

            if following_production:
                result["following_production"] = self.format_output_dict(following_production)

        return result
