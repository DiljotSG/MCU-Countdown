import unittest
from datetime import date

from src.objects.production import Production


class TestProduction(unittest.TestCase):
    def test_from_tmdb_dict_movie(self):
        data = {
            "id": 12345,
            "original_title": "Test Movie",
            "release_date": "2025-06-15",
            "poster_path": "/poster.jpg",
            "overview": "A test movie",
            "media_type": "movie",
        }

        production = Production.from_tmdb_dict(data)

        self.assertEqual(production.id, 12345)
        self.assertEqual(production.title, "Test Movie")
        self.assertEqual(production.release_date, date(2025, 6, 15))
        self.assertEqual(production.poster_path, "/poster.jpg")
        self.assertEqual(production.overview, "A test movie")
        self.assertEqual(production.media_type, "movie")

    def test_from_tmdb_dict_tv_show(self):
        data = {
            "id": 67890,
            "original_name": "Test Show",
            "first_air_date": "2025-09-01",
            "poster_path": "/poster.jpg",
            "overview": "A test show",
            "media_type": "tv",
        }

        production = Production.from_tmdb_dict(data)

        self.assertEqual(production.id, 67890)
        self.assertEqual(production.title, "Test Show")
        self.assertEqual(production.release_date, date(2025, 9, 1))
        self.assertEqual(production.media_type, "tv")

    def test_from_tmdb_dict_no_date(self):
        data = {
            "id": 12345,
            "original_title": "No Date Movie",
            "poster_path": "/poster.jpg",
            "overview": "A movie with no date",
            "media_type": "movie",
        }

        production = Production.from_tmdb_dict(data)

        self.assertIsNone(production.release_date)

    def test_display_type_movie(self):
        production = Production(
            id=1,
            title="Test",
            release_date=None,
            poster_path=None,
            overview=None,
            media_type="movie",
        )
        self.assertEqual(production.display_type, "Movie")

    def test_display_type_tv(self):
        production = Production(
            id=1,
            title="Test",
            release_date=None,
            poster_path=None,
            overview=None,
            media_type="tv",
        )
        self.assertEqual(production.display_type, "TV Show")

    def test_days_until_release(self):
        production = Production(
            id=1,
            title="Test",
            release_date=date(2025, 6, 15),
            poster_path=None,
            overview=None,
            media_type="movie",
        )

        days = production.days_until_release(from_date=date(2025, 6, 10))
        self.assertEqual(days, 5)

    def test_days_until_release_no_date(self):
        production = Production(
            id=1,
            title="Test",
            release_date=None,
            poster_path=None,
            overview=None,
            media_type="movie",
        )

        days = production.days_until_release()
        self.assertIsNone(days)
