from datetime import MAXYEAR, date
from typing import List, Optional, Tuple

from src.consts import TMDB_DEFAULT_LIST
from src.exceptions import ListNotFoundError, NoUpcomingProductionsError
from src.objects.production import Production
from src.services.tmdb import TMDBService


class Oracle:
    def __init__(self):
        self.tmdb: TMDBService = TMDBService()
        self.max_date = date(MAXYEAR, 1, 1)

    def _fetch_production_list(
        self, tmdb_list_id: Optional[int] = None
    ) -> List[Production]:
        list_id = tmdb_list_id if tmdb_list_id else TMDB_DEFAULT_LIST
        response = self.tmdb.get_last_page_list(list_id)

        if not response:
            raise ListNotFoundError(list_id)

        production_list = response.get("items", [])

        if not production_list:
            raise ListNotFoundError(list_id, f"List {list_id} exists but has no items")

        return [Production.from_tmdb_dict(item) for item in production_list]

    def _find_next_after_date(
        self,
        productions: List[Production],
        desired_date: date,
        list_id: Optional[int] = None,
    ) -> Tuple[Production, Optional[Production]]:
        for i, prod in enumerate(productions):
            release_date = prod.release_date if prod.release_date else self.max_date

            if release_date > desired_date:
                next_production = prod
                following_production = (
                    productions[i + 1] if i + 1 < len(productions) else None
                )
                return next_production, following_production

        raise NoUpcomingProductionsError(
            list_id=list_id, desired_date=desired_date.isoformat()
        )

    def get_next_production(
        self,
        production_list: Optional[List[Production]] = None,
        desired_date: Optional[date] = None,
        tmdb_list_id: Optional[int] = None,
    ) -> Tuple[Production, Optional[Production]]:
        if not production_list:
            production_list = self._fetch_production_list(tmdb_list_id)

        if desired_date is None:
            desired_date = date.today()

        actual_list_id = tmdb_list_id if tmdb_list_id else TMDB_DEFAULT_LIST

        return self._find_next_after_date(production_list, desired_date, actual_list_id)

    def format_output_dict(self, production: Production) -> Optional[dict]:
        if production.release_date is None:
            return None

        days_until = production.days_until_release()

        return {
            "release_date": production.release_date.isoformat(),
            "title": production.title,
            "poster_url": (
                self.tmdb.give_poster_url(production.poster_path)
                if production.poster_path
                else None
            ),
            "overview": production.overview,
            "days_until": days_until,
            "type": production.display_type,
            "id": production.id,
        }

    def get_next_mcu_production(
        self,
        desired_date: Optional[date] = None,
        tmdb_list_id: Optional[int] = None,
    ) -> dict:
        try:
            next_production, following_production = self.get_next_production(
                desired_date=desired_date, tmdb_list_id=tmdb_list_id
            )
        except (ListNotFoundError, NoUpcomingProductionsError):
            return {}

        result = self.format_output_dict(next_production)

        if result is None:
            return {}

        if following_production:
            following_result = self.format_output_dict(following_production)
            if following_result:
                result["following_production"] = following_result

        return result
