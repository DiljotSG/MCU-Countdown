import unittest
from unittest.mock import patch

import src


class TestAPI(unittest.TestCase):
    def setUp(self):
        app = src.create_flask_app()
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_get_root_with_data(self, mock_get_next):
        # Mock a successful response
        mock_get_next.return_value = {
            "title": "Test Movie",
            "release_date": "2025-12-01",
            "days_until": 100,
            "overview": "Test overview",
            "type": "Movie",
            "poster_url": "https://example.com/poster.jpg",
            "following_production": {"title": "Next Movie"},
        }

        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Movie", response.data)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_get_root_no_data(self, mock_get_next):
        # Mock empty response
        mock_get_next.return_value = {}

        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_get_api(self, mock_get_next):
        # Mock a successful response
        mock_get_next.return_value = {
            "title": "Test Movie",
            "release_date": "2025-12-01",
            "days_until": 100,
        }

        response = self.app.get("/api", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Movie", response.data)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_api_with_date_parameter(self, mock_get_next):
        mock_get_next.return_value = {
            "title": "Future Movie",
            "release_date": "2030-01-01",
            "days_until": 1500,
        }

        response = self.app.get("/api?date=2025-01-01", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Future Movie", response.data)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_api_with_custom_list_id(self, mock_get_next):
        mock_get_next.return_value = {
            "title": "Custom List Movie",
            "release_date": "2025-06-01",
            "days_until": 200,
        }

        response = self.app.get("/api?list_id=12345", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        mock_get_next.assert_called_once()

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_api_with_invalid_date(self, mock_get_next):
        mock_get_next.return_value = {
            "title": "Test Movie",
            "release_date": "2025-12-01",
            "days_until": 100,
        }

        response = self.app.get("/api?date=invalid-date", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Should fall back to default behavior

    def test_cache_headers_present(self):
        with patch(
            "src.services.oracle.Oracle.get_next_mcu_production"
        ) as mock_get_next:
            mock_get_next.return_value = {
                "title": "Test Movie",
                "release_date": "2025-12-01",
                "days_until": 100,
            }

            response = self.app.get("/api")
            self.assertIn("Cache-Control", response.headers)
            self.assertIn("max-age", response.headers["Cache-Control"])

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_named_route_star_wars(self, mock_get_next):
        mock_get_next.return_value = {
            "title": "Star Wars Movie",
            "release_date": "2025-12-01",
            "days_until": 100,
            "overview": "Test overview",
            "type": "Movie",
            "poster_url": "https://example.com/poster.jpg",
            "following_production": {},
        }

        response = self.app.get("/star-wars")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Star Wars Movie", response.data)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_named_route_dc(self, mock_get_next):
        mock_get_next.return_value = {
            "title": "DC Movie",
            "release_date": "2025-12-01",
            "days_until": 100,
            "overview": "Test overview",
            "type": "Movie",
            "poster_url": "https://example.com/poster.jpg",
            "following_production": {},
        }

        response = self.app.get("/dc")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"DC Movie", response.data)

    def test_named_route_invalid(self):
        response = self.app.get("/invalid-list-name")
        self.assertEqual(response.status_code, 404)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_named_route_ignores_list_id_param(self, mock_get_next):
        mock_get_next.return_value = {
            "title": "Star Wars Movie",
            "release_date": "2025-12-01",
            "days_until": 100,
            "overview": "Test overview",
            "type": "Movie",
            "poster_url": "https://example.com/poster.jpg",
            "following_production": {},
        }

        # list_id parameter should be ignored for named routes
        response = self.app.get("/star-wars?list_id=99999")
        self.assertEqual(response.status_code, 200)
        # Should still call with the Star Wars list_id (8563040), not 99999
        mock_get_next.assert_called_once()
        call_kwargs = mock_get_next.call_args.kwargs
        self.assertEqual(call_kwargs.get("tmdb_list_id"), 8563040)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_named_route_dc_uses_correct_list_id(self, mock_get_next):
        mock_get_next.return_value = {
            "title": "DC Movie",
            "release_date": "2025-12-01",
            "days_until": 100,
            "overview": "Test overview",
            "type": "Movie",
            "poster_url": "https://example.com/poster.jpg",
            "following_production": {},
        }

        response = self.app.get("/dc")
        self.assertEqual(response.status_code, 200)
        # Verify it uses the correct DC list_id (8563041)
        mock_get_next.assert_called_once()
        call_kwargs = mock_get_next.call_args.kwargs
        self.assertEqual(call_kwargs.get("tmdb_list_id"), 8563041)

    @patch("src.services.oracle.Oracle.get_next_mcu_production")
    def test_named_route_batman(self, mock_get_next):
        mock_get_next.return_value = {
            "title": "The Batman Movie",
            "release_date": "2025-12-01",
            "days_until": 100,
            "overview": "Test overview",
            "type": "Movie",
            "poster_url": "https://example.com/poster.jpg",
            "following_production": {},
        }

        response = self.app.get("/batman")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The Batman", response.data)
        # Verify it uses the correct Batman list_id (8563043)
        mock_get_next.assert_called_once()
        call_kwargs = mock_get_next.call_args.kwargs
        self.assertEqual(call_kwargs.get("tmdb_list_id"), 8563043)
