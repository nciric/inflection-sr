import exceptions as ex
import unittest


class TestExceptions(unittest.TestCase):

    def test_has_it(self):
        result = ex.return_exception('кћи')
        self.assertIsInstance(result, list)
        self.assertEqual(14, len(result))

    def test_doesnt_have_it(self):
        self.assertEqual(None, ex.return_exception('not in there'))


if __name__ == '__main__':
    unittest.main()
