import src
import unittest


class TestAPI(unittest.TestCase):

    def setUp(self):
        app = src.create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_get_root(self):
        response = self.app.get(
            "/",
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 404)

    def test_get_api(self):
        response = self.app.get(
            "/api",
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
