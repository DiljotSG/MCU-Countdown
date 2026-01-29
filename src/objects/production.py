from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Production:
    id: int
    title: str
    release_date: Optional[date]
    poster_path: Optional[str]
    overview: Optional[str]
    media_type: str

    @classmethod
    def from_tmdb_dict(cls, data: dict) -> "Production":
        media_type = data.get("media_type", "movie")
        title = data.get("original_title") or data.get("original_name")
        date_str = data.get("release_date") or data.get("first_air_date")
        release_date = date.fromisoformat(date_str) if date_str else None

        return cls(
            id=data.get("id", -1),
            title=title,
            release_date=release_date,
            poster_path=data.get("poster_path"),
            overview=data.get("overview"),
            media_type=media_type,
        )

    @property
    def display_type(self) -> str:
        return "TV Show" if self.media_type == "tv" else "Movie"

    def days_until_release(self, from_date: Optional[date] = None) -> Optional[int]:
        if self.release_date is None:
            return None

        if from_date is None:
            from_date = date.today()

        return (self.release_date - from_date).days
