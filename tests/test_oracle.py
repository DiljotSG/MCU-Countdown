import unittest
from src.services.oracle import Oracle


class TestOracle(unittest.TestCase):

    def setUp(self):
        self.oracle = Oracle()

    def test_get_next_production(self):
        sample_date = "2020-01-01"
        expected_next_production = {
            "title": "Sample Film 3",
            "release_date": "2028-04-30"
        }
        production_list = [
            {
                "title": "Sample Film 1",
                "release_date": "2008-04-30"
            },
            {
                "title": "Sample Film 2",
                "release_date": "2018-04-30"
            },
            expected_next_production
        ]
        next_production = self.oracle.get_next_production(production_list, sample_date)[0]
        self.assertEqual(expected_next_production, next_production)
