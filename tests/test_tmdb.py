import os
import unittest
from unittest.mock import patch

from src.services import tmdb
from src.services.tmdb import TMDBService


class TestTMDBService(unittest.TestCase):
    def setUp(self):
        self.original_api_key = os.environ.get("TMDB_API_KEY")
        if "TMDB_API_KEY" in os.environ:
            del os.environ["TMDB_API_KEY"]
        self.tmdb = TMDBService(api_key="test_api_key")
        tmdb._list_cache.clear()
        tmdb._last_page_cache.clear()

    def tearDown(self):
        tmdb._list_cache.clear()
        tmdb._last_page_cache.clear()
        if self.original_api_key:
            os.environ["TMDB_API_KEY"] = self.original_api_key

    def test_get_no_api_key(self):
        tmdb_no_key = TMDBService(api_key=None)
        result = tmdb_no_key._get("/list/123")
        self.assertIsNone(result)

    def test_give_poster_url(self):
        expected = "https://image.tmdb.org/t/p/w500/path/to/poster.jpg"
        result = self.tmdb.give_poster_url("/path/to/poster.jpg")
        self.assertEqual(result, expected)

    @patch.object(TMDBService, "_get")
    def test_get_list(self, mock_get):
        mock_get.return_value = {
            "page": 1,
            "total_pages": 1,
            "items": [{"id": 1, "title": "Test Movie"}],
        }

        result = self.tmdb.get_list(12345)

        self.assertIsNotNone(result)
        self.assertEqual(result["page"], 1)
        self.assertEqual(len(result["items"]), 1)

    @patch.object(TMDBService, "_get")
    def test_get_list_caching(self, mock_get):
        mock_get.return_value = {"page": 1, "total_pages": 1, "items": []}

        result1 = self.tmdb.get_list(12345)
        self.assertEqual(mock_get.call_count, 1)

        result2 = self.tmdb.get_list(12345)
        self.assertEqual(mock_get.call_count, 1)

        self.assertEqual(result1, result2)

    @patch.object(TMDBService, "get_list")
    def test_get_last_page_list_single_page(self, mock_get_list):
        mock_get_list.return_value = {"page": 1, "total_pages": 1, "items": [{"id": 1}]}

        result = self.tmdb.get_last_page_list(12345)

        self.assertEqual(result["page"], 1)
        self.assertEqual(mock_get_list.call_count, 1)

    @patch.object(TMDBService, "get_list")
    def test_get_last_page_list_multiple_pages(self, mock_get_list):
        def side_effect(list_num, page_num=1):
            if page_num == 1:
                return {"page": 1, "total_pages": 3, "items": [{"id": 1}]}
            elif page_num == 3:
                return {"page": 3, "total_pages": 3, "items": [{"id": 3}]}
            return None

        mock_get_list.side_effect = side_effect

        result = self.tmdb.get_last_page_list(12345)

        self.assertEqual(result["page"], 3)
        self.assertEqual(mock_get_list.call_count, 2)

    @patch.object(TMDBService, "get_list")
    def test_get_last_page_list_none_response(self, mock_get_list):
        mock_get_list.return_value = None

        result = self.tmdb.get_last_page_list(12345)

        self.assertIsNone(result)

    @patch.object(TMDBService, "get_list")
    def test_get_last_page_list_caching(self, mock_get_list):
        mock_get_list.return_value = {"page": 1, "total_pages": 1, "items": [{"id": 1}]}

        result1 = self.tmdb.get_last_page_list(12345)
        call_count_first = mock_get_list.call_count

        result2 = self.tmdb.get_last_page_list(12345)
        call_count_second = mock_get_list.call_count

        self.assertEqual(call_count_first, call_count_second)
        self.assertEqual(result1, result2)
