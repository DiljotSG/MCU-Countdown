import unittest
from datetime import date
from unittest.mock import patch

from src.exceptions import NoUpcomingProductionsError
from src.objects.production import Production
from src.services.oracle import Oracle


class TestOracle(unittest.TestCase):
    def setUp(self):
        self.oracle = Oracle()

    def _make_productions(self, items: list) -> list:
        return [Production.from_tmdb_dict(item) for item in items]

    def test_get_next_production(self):
        sample_date = date(2020, 1, 1)
        production_list = self._make_productions(
            [
                {"original_title": "Sample Film 1", "release_date": "2008-04-30"},
                {"original_title": "Sample Film 2", "release_date": "2018-04-30"},
                {"original_title": "Sample Film 3", "release_date": "2028-04-30"},
            ]
        )
        result = self.oracle.get_next_production(production_list, sample_date)
        next_production, _ = result
        self.assertEqual(next_production.title, "Sample Film 3")
        self.assertEqual(next_production.release_date, date(2028, 4, 30))

    def test_get_next_production_with_tv_show(self):
        sample_date = date(2020, 1, 1)
        production_list = self._make_productions(
            [
                {"original_title": "Sample Film", "release_date": "2008-04-30"},
                {
                    "original_name": "Sample Show",
                    "first_air_date": "2028-04-30",
                    "media_type": "tv",
                },
            ]
        )
        result = self.oracle.get_next_production(production_list, sample_date)
        self.assertIsNotNone(result)
        next_production, _ = result
        self.assertEqual(next_production.release_date, date(2028, 4, 30))
        self.assertEqual(next_production.media_type, "tv")

    def test_get_next_production_no_future_releases(self):
        sample_date = date(2030, 1, 1)
        production_list = self._make_productions(
            [{"original_title": "Past Film", "release_date": "2020-04-30"}]
        )
        with self.assertRaises(NoUpcomingProductionsError):
            self.oracle.get_next_production(production_list, sample_date)

    def test_get_next_production_with_following(self):
        sample_date = date(2020, 1, 1)
        production_list = self._make_productions(
            [
                {"original_title": "Past Film", "release_date": "2010-04-30"},
                {"original_title": "Next Film", "release_date": "2025-04-30"},
                {"original_title": "Following Film", "release_date": "2026-04-30"},
            ]
        )
        result = self.oracle.get_next_production(production_list, sample_date)
        next_production, following_production = result
        self.assertIsNotNone(next_production)
        self.assertIsNotNone(following_production)
        self.assertEqual(next_production.title, "Next Film")
        self.assertEqual(following_production.title, "Following Film")

    @patch("src.services.tmdb.TMDBService.get_last_page_list")
    def test_get_next_production_from_tmdb(self, mock_get_list):
        mock_get_list.return_value = {
            "items": [{"original_title": "Future Film", "release_date": "2030-01-01"}]
        }

        result = self.oracle.get_next_production(desired_date=date(2025, 1, 1))
        self.assertIsNotNone(result)
        next_production, _ = result
        self.assertEqual(next_production.title, "Future Film")

    def test_format_output_dict_movie(self):
        production = Production(
            id=12345,
            title="Test Movie",
            release_date=date(2025, 12, 31),
            poster_path="/test.jpg",
            overview="Test overview",
            media_type="movie",
        )

        result = self.oracle.format_output_dict(production)

        self.assertEqual(result["title"], "Test Movie")
        self.assertEqual(result["release_date"], "2025-12-31")
        self.assertEqual(result["type"], "Movie")
        self.assertEqual(result["id"], 12345)
        self.assertIn("days_until", result)

    def test_format_output_dict_tv_show(self):
        production = Production(
            id=67890,
            title="Test Show",
            release_date=date(2025, 6, 15),
            poster_path="/test.jpg",
            overview="Test overview",
            media_type="tv",
        )

        result = self.oracle.format_output_dict(production)

        self.assertEqual(result["title"], "Test Show")
        self.assertEqual(result["release_date"], "2025-06-15")
        self.assertEqual(result["type"], "TV Show")
        self.assertEqual(result["id"], 67890)

    def test_format_output_dict_no_release_date(self):
        production = Production(
            id=12345,
            title="Test Movie",
            release_date=None,
            poster_path="/test.jpg",
            overview="Test overview",
            media_type="movie",
        )

        result = self.oracle.format_output_dict(production)

        self.assertIsNone(result)

    def test_format_output_dict_none_values(self):
        production = Production(
            id=12345,
            title="Test Movie",
            release_date=date(2025, 12, 31),
            poster_path=None,
            overview=None,
            media_type="movie",
        )

        result = self.oracle.format_output_dict(production)

        self.assertIsNone(result["poster_url"])
        self.assertIsNone(result["overview"])

    def test_get_next_mcu_production(self):
        with patch.object(self.oracle, "get_next_production") as mock_get_next:
            mock_get_next.return_value = (
                Production(
                    id=12345,
                    title="Next MCU Film",
                    release_date=date(2025, 5, 1),
                    poster_path="/poster.jpg",
                    overview="Next MCU film",
                    media_type="movie",
                ),
                Production(
                    id=12346,
                    title="Following MCU Film",
                    release_date=date(2025, 11, 1),
                    poster_path="/poster2.jpg",
                    overview="Following film",
                    media_type="movie",
                ),
            )

            result = self.oracle.get_next_mcu_production()

            self.assertIn("title", result)
            self.assertIn("following_production", result)
            self.assertEqual(result["title"], "Next MCU Film")
            self.assertEqual(
                result["following_production"]["title"], "Following MCU Film"
            )

    @patch("src.services.oracle.Oracle.get_next_production")
    def test_get_next_mcu_production_with_custom_list(self, mock_get_next):
        mock_get_next.return_value = (
            Production(
                id=999,
                title="Custom List Film",
                release_date=date(2025, 7, 1),
                poster_path="/poster.jpg",
                overview="Custom film",
                media_type="movie",
            ),
            None,
        )

        result = self.oracle.get_next_mcu_production(tmdb_list_id=12345)

        self.assertEqual(result["title"], "Custom List Film")
        mock_get_next.assert_called_once()
        call_args = mock_get_next.call_args
        self.assertEqual(call_args.kwargs.get("tmdb_list_id"), 12345)

    @patch("src.services.oracle.Oracle.get_next_production")
    def test_get_next_mcu_production_empty_result(self, mock_get_next):
        mock_get_next.side_effect = NoUpcomingProductionsError()

        result = self.oracle.get_next_mcu_production()

        self.assertEqual(result, {})
