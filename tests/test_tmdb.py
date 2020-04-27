import unittest
from src.services.tmdb import TMDBService


class TestTMDBService(unittest.TestCase):

    def setUp(self):
        self.tmdb = TMDBService(
            api_key="CXdrQrBgAL3HET3mMmMt"  # Random Str
        )

    def test_send_request(self):
        expected_data = "https://api.themoviedb.org/3/lists?api_key=CXdrQrBgAL3HET3mMmMt&language=en-CA"
        data = self.tmdb.send_request("lists").url
        self.assertEqual(data, expected_data)

    def test_give_poster_url(self):
        expected_data = "https://image.tmdb.org/t/p/w500/path/to/poster.jpg"
        data = self.tmdb.give_poster_url("/path/to/poster.jpg")
        self.assertEqual(data, expected_data)
