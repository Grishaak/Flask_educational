import unittest
from apps.usual.app import app


class TestRouteMaxFlask(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/max-number/'

    def test_max_number(self):
        numbers = 1, 2
        url = self.base_url + "/".join(str(i) for i in numbers)
        response = self.app.get(url)
        response_text = response.data.decode()
        correct_answer_str = f"<b>{max(numbers)}</b>"
        print(correct_answer_str)
        print(response_text)
        self.assertTrue(correct_answer_str in response_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
