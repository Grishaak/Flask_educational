import unittest

from apps.usual.app import app


class TestRouteHelloFlask(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_hello_world(self):
        from datetime import datetime
        name = 'Sergey'
        url = self.base_url + name
        response = self.app.get(url)
        response_text = response.data.decode()
        weekday = datetime.now().strftime("%A")
        correct_answer_str = f"Hello, Sergey, today is {weekday}"
        self.assertTrue(correct_answer_str in response_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
