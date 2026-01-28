import unittest
from unittest.mock import patch

from src.exceptions import NoUpcomingProductionsError
from src.services.oracle import Oracle


class TestOracle(unittest.TestCase):
    def setUp(self):
        self.oracle = Oracle()

    def test_get_next_production(self):
        sample_date = "2020-01-01"
        expected_next_production = {
            "title": "Sample Film 3",
            "release_date": "2028-04-30",
        }
        production_list = [
            {"title": "Sample Film 1", "release_date": "2008-04-30"},
            {"title": "Sample Film 2", "release_date": "2018-04-30"},
            expected_next_production,
        ]
        result = self.oracle.get_next_production(production_list, sample_date)
        # Result is now a tuple (next_production, following_production)
        next_production, following_production = result
        self.assertEqual(expected_next_production, next_production)

    def test_get_next_production_with_tv_show(self):
        sample_date = "2020-01-01"
        production_list = [
            {"title": "Sample Film", "release_date": "2008-04-30"},
            {
                "original_name": "Sample Show",
                "first_air_date": "2028-04-30",
                "media_type": "tv",
            },
        ]
        result = self.oracle.get_next_production(production_list, sample_date)
        self.assertIsNotNone(result)
        # Result is now a tuple
        next_production, following_production = result
        self.assertEqual(next_production["first_air_date"], "2028-04-30")

    def test_get_next_production_no_future_releases(self):
        sample_date = "2030-01-01"
        production_list = [{"title": "Past Film", "release_date": "2020-04-30"}]
        # Should now raise an exception instead of returning None
        with self.assertRaises(NoUpcomingProductionsError):
            self.oracle.get_next_production(production_list, sample_date)

    def test_get_next_production_with_following(self):
        sample_date = "2020-01-01"
        production_list = [
            {"title": "Past Film", "release_date": "2010-04-30"},
            {"title": "Next Film", "release_date": "2025-04-30"},
            {"title": "Following Film", "release_date": "2026-04-30"},
        ]
        result = self.oracle.get_next_production(production_list, sample_date)
        # Result is now a tuple
        next_production, following_production = result
        self.assertIsNotNone(next_production)
        self.assertIsNotNone(following_production)
        self.assertEqual(next_production["title"], "Next Film")
        self.assertEqual(following_production["title"], "Following Film")

    @patch("src.services.tmdb.TMDBService.get_last_page_list")
    def test_get_next_production_from_tmdb(self, mock_get_list):
        mock_get_list.return_value = {
            "items": [{"title": "Future Film", "release_date": "2030-01-01"}]
        }

        result = self.oracle.get_next_production(desired_date="2025-01-01")
        self.assertIsNotNone(result)
        # Result is now a tuple
        next_production, following_production = result
        self.assertEqual(next_production["title"], "Future Film")

    def test_format_output_dict_movie(self):
        tmdb_item = {
            "original_title": "Test Movie",
            "release_date": "2025-12-31",
            "poster_path": "/test.jpg",
            "overview": "Test overview",
            "media_type": "movie",
            "id": 12345,
        }

        result = self.oracle.format_output_dict(tmdb_item)

        self.assertEqual(result["title"], "Test Movie")
        self.assertEqual(result["release_date"], "2025-12-31")
        self.assertEqual(result["type"], "Movie")
        self.assertEqual(result["id"], 12345)
        self.assertIn("days_until", result)

    def test_format_output_dict_tv_show(self):
        tmdb_item = {
            "original_name": "Test Show",
            "first_air_date": "2025-06-15",
            "poster_path": "/test.jpg",
            "overview": "Test overview",
            "media_type": "tv",
            "id": 67890,
        }

        result = self.oracle.format_output_dict(tmdb_item)

        self.assertEqual(result["title"], "Test Show")
        self.assertEqual(result["release_date"], "2025-06-15")
        self.assertEqual(result["type"], "TV Show")
        self.assertEqual(result["id"], 67890)

    def test_format_output_dict_no_release_date(self):
        tmdb_item = {
            "original_title": "Test Movie",
            "poster_path": "/test.jpg",
            "overview": "Test overview",
            "media_type": "movie",
            "id": 12345,
        }

        result = self.oracle.format_output_dict(tmdb_item)

        # Should return empty dict if no release date
        self.assertEqual(result, {})

    def test_get_next_mcu_production(self):
        # Mock the production data
        with patch.object(
            self.oracle, "get_next_production"
        ) as mock_get_next:
            mock_get_next.return_value = (
                {
                    "original_title": "Next MCU Film",
                    "release_date": "2025-05-01",
                    "poster_path": "/poster.jpg",
                    "overview": "Next MCU film",
                    "media_type": "movie",
                    "id": 12345,
                },
                {
                    "original_title": "Following MCU Film",
                    "release_date": "2025-11-01",
                    "poster_path": "/poster2.jpg",
                    "overview": "Following film",
                    "media_type": "movie",
                    "id": 12346,
                },
            )

            result = self.oracle.get_next_mcu_production()

            self.assertIn("title", result)
            self.assertIn("following_production", result)
            self.assertEqual(result["title"], "Next MCU Film")
            self.assertEqual(result["following_production"]["title"], "Following MCU Film")

    @patch("src.services.oracle.Oracle.get_next_production")
    def test_get_next_mcu_production_with_custom_list(self, mock_get_next):
        # Mock returns a tuple (next_production, following_production)
        mock_get_next.return_value = (
            {
                "original_title": "Custom List Film",
                "release_date": "2025-07-01",
                "poster_path": "/poster.jpg",
                "overview": "Custom film",
                "media_type": "movie",
                "id": 999,
            },
            None,  # No following production
        )

        result = self.oracle.get_next_mcu_production(tmdb_list_id=12345)

        self.assertEqual(result["title"], "Custom List Film")
        # Verify that get_next_production was called with the custom list_id
        mock_get_next.assert_called_once()
        call_args = mock_get_next.call_args
        self.assertEqual(call_args.kwargs.get("tmdb_list_id"), 12345)

    @patch("src.services.oracle.Oracle.get_next_production")
    def test_get_next_mcu_production_empty_result(self, mock_get_next):
        mock_get_next.return_value = None

        result = self.oracle.get_next_mcu_production()

        self.assertEqual(result, {})
