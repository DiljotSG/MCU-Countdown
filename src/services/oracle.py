from datetime import date
from datetime import MAXYEAR
from datetime import timedelta
from src.services.tmdb import TMDBService
from src.constants.values import TMDB_MCU_LIST

from typing import Optional


class Oracle:
    def __init__(self):
        self.tmdb: TMDBService = TMDBService()
        self.max_date = "{}-01-01".format(MAXYEAR)

    def get_next_movie(
        self,
        movie_list: Optional[dict] = None,
        desired_date: Optional[str] = None
    ) -> Optional[dict]:
        if not movie_list:
            movie_list = self.tmdb.get_list(TMDB_MCU_LIST)

        if movie_list:

            # Use the current date if we are not passed one
            if not desired_date:
                # Get the current date in ISO format
                desired_date = date.today().isoformat()

            try:
                # Find the first film with a release date larger than the current date
                index: int = next(i for i, v in enumerate(movie_list) if v.get("release_date", self.max_date) > desired_date)
                if index:
                    return movie_list[index]
            except StopIteration:
                pass

        return None

    def get_next_movie_html(self) -> str:
        next_movie: dict = self.get_next_movie_json()
        return "{} Days Until {}".format(next_movie.get("days_until", ""), next_movie.get("title", ""))

    def get_next_movie_json(
        self,
        desired_date: Optional[str] = None
    ) -> dict:
        result: dict = {}
        next_movie: Optional[dict] = self.get_next_movie(
            desired_date=desired_date
        )

        if next_movie:
            # Days until the movies' release
            days_until: timedelta = date.fromisoformat(next_movie.get("release_date", self.max_date)) - date.today()

            # Format the result dictionary
            result["title"] = next_movie["original_title"]
            result["release_date"] = next_movie.get("release_date", self.max_date)
            result["poster_path"] = self.tmdb.give_poster_url(next_movie["poster_path"])
            result["overview"] = next_movie["overview"]
            result["days_until"] = int(days_until.days)

        return result
