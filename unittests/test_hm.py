import unittest
from hm.hm_3 import decoder


class TestHm(unittest.TestCase):

    def test_decoder(self):
        result = decoder("Мумба...-..-Ю...Мбааа")
        print(result)
        expected = 'Мумб-Мбааа'
        self.assertEqual(result, expected)

    def test_decoder_type_error(self):
        with self.assertRaises(ValueError):
            decoder(12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
