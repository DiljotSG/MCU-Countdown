import os
import unittest
from unittest.mock import MagicMock, patch

from src.services.tmdb import TMDBService


class TestTMDBService(unittest.TestCase):
    def setUp(self):
        # Clear cache before each test
        # Temporarily clear TMDB_API_KEY env var for tests
        self.original_api_key = os.environ.get("TMDB_API_KEY")
        if "TMDB_API_KEY" in os.environ:
            del os.environ["TMDB_API_KEY"]
        self.tmdb = TMDBService(api_key="CXdrQrBgAL3HET3mMmMt")  # Random Str
        self.tmdb.cache.clear()

    def tearDown(self):
        # Clean up cache after each test
        self.tmdb.cache.clear()
        # Restore original API key
        if self.original_api_key:
            os.environ["TMDB_API_KEY"] = self.original_api_key

    def test_send_request(self):
        expected_data = "https://api.themoviedb.org/3/lists?api_key=CXdrQrBgAL3HET3mMmMt&language=en-CA&page=1"
        data = self.tmdb.send_request("lists").url
        self.assertEqual(data, expected_data)

    def test_send_request_no_api_key(self):
        tmdb_no_key = TMDBService(api_key=None)
        result = tmdb_no_key.send_request("lists")
        self.assertIsNone(result)

    def test_give_poster_url(self):
        expected_data = "https://image.tmdb.org/t/p/w500/path/to/poster.jpg"
        data = self.tmdb.give_poster_url("/path/to/poster.jpg")
        self.assertEqual(data, expected_data)

    @patch("src.services.tmdb.TMDBService.send_request")
    def test_get_list(self, mock_send_request):
        # Mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "items": [{"id": 1, "title": "Test Movie"}],
        }
        mock_send_request.return_value = mock_response

        result = self.tmdb.get_list(12345)

        self.assertIsNotNone(result)
        self.assertEqual(result["page"], 1)
        self.assertEqual(len(result["items"]), 1)
        mock_send_request.assert_called_once()

    @patch("src.services.tmdb.TMDBService.send_request")
    def test_get_list_caching(self, mock_send_request):
        # Mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"page": 1, "total_pages": 1, "items": []}
        mock_send_request.return_value = mock_response

        # First call should hit the API
        result1 = self.tmdb.get_list(12345)
        self.assertEqual(mock_send_request.call_count, 1)

        # Second call should use cache
        result2 = self.tmdb.get_list(12345)
        self.assertEqual(mock_send_request.call_count, 1)  # Still 1, not 2

        # Results should be identical
        self.assertEqual(result1, result2)

    @patch("src.services.tmdb.TMDBService.get_list")
    def test_get_last_page_list_single_page(self, mock_get_list):
        # Mock a single-page list
        mock_get_list.return_value = {"page": 1, "total_pages": 1, "items": [{"id": 1}]}

        result = self.tmdb.get_last_page_list(12345)

        self.assertEqual(result["page"], 1)
        self.assertEqual(mock_get_list.call_count, 1)

    @patch("src.services.tmdb.TMDBService.get_list")
    def test_get_last_page_list_multiple_pages(self, mock_get_list):
        # Mock a multi-page list
        def side_effect(list_num, page_num=1):
            if page_num == 1:
                return {"page": 1, "total_pages": 3, "items": [{"id": 1}]}
            elif page_num == 3:
                return {"page": 3, "total_pages": 3, "items": [{"id": 3}]}

        mock_get_list.side_effect = side_effect

        result = self.tmdb.get_last_page_list(12345)

        self.assertEqual(result["page"], 3)
        self.assertEqual(mock_get_list.call_count, 2)  # Called twice: page 1 and page 3

    @patch("src.services.tmdb.TMDBService.get_list")
    def test_get_last_page_list_none_response(self, mock_get_list):
        mock_get_list.return_value = None

        result = self.tmdb.get_last_page_list(12345)

        self.assertIsNone(result)

    @patch("src.services.tmdb.TMDBService.get_list")
    def test_get_last_page_list_caching(self, mock_get_list):
        mock_get_list.return_value = {"page": 1, "total_pages": 1, "items": [{"id": 1}]}

        # First call
        result1 = self.tmdb.get_last_page_list(12345)
        call_count_first = mock_get_list.call_count

        # Second call should use cache
        result2 = self.tmdb.get_last_page_list(12345)
        call_count_second = mock_get_list.call_count

        # Call count should be the same (cached)
        self.assertEqual(call_count_first, call_count_second)
        self.assertEqual(result1, result2)
