import unittest

from apps.app_wtf import app


class TestEndpointPostRequest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/registration'

    def test_registration(self):
        url = self.base_url
        email = 'test@gmail.com'
        response = self.app.post(url, ('email', email))
        response_text = response.data.decode()
        print(response_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
