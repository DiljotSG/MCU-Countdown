from datetime import date
from datetime import timedelta
from src.services.tmdb import TMDBService
from src.constants.values import TMDB_MCU_LIST

from typing import Optional


class Oracle:
    def __init__(self):
        self.tmdb: TMDBService = TMDBService()

    def __get_next_movie(self) -> Optional[dict]:
        mcu_list: list = self.tmdb.get_list(TMDB_MCU_LIST)

        # Get the current date in ISO format
        curr_date: date = date.today().isoformat()

        # Find the first film with a release date larger than the current date
        index: int = next(i for i, v in enumerate(mcu_list) if v["release_date"] > curr_date)
        if index:
            return mcu_list[index]
        return None

    def get_next_movie_html(self) -> str:
        next_movie: dict = self.get_next_movie_json()
        return "{} Days Until {}".format(next_movie.get("days_until", ""), next_movie.get("title", ""))

    def get_next_movie_json(self) -> dict:
        result: dict = {}
        next_movie: Optional[dict] = self.__get_next_movie()

        if next_movie:
            # Days until the movies' release
            days_until: timedelta = date.fromisoformat(next_movie["release_date"]) - date.today()

            # Format the result dictionary
            result["title"] = next_movie["original_title"]
            result["release_date"] = next_movie["release_date"]
            result["poster_path"] = self.tmdb.get_poster_url(next_movie["poster_path"])
            result["overview"] = next_movie["overview"]
            result["days_until"] = int(days_until.days)

        return result
