import unittest
from hm.person_to_test import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person("Иван", 1977, "Wolf Street")

    def test_name(self):
        self.assertEqual('Иван', self.person.get_name())

    def test_age(self):
        self.assertEqual(47, self.person.get_age())

    def test_address(self):
        self.assertEqual("Wolf Street", self.person.get_address())

    def test_set_name(self):
        self.person.set_name("Вася")
        self.assertEqual("Вася", self.person.get_name())

    def test_set_address(self):
        self.person.set_address("Dragon Street")
        self.assertEqual("Dragon Street", self.person.get_address())

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless())


if __name__ == '__main__':
    unittest.main(verbosity=1)
