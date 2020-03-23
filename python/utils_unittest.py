import utils
import unittest


class TestUtils(unittest.TestCase):

    def test_is_multisyllabic(self):
        self.assertTrue(utils.is_multisyllabic('Небојша'))
        self.assertTrue(utils.is_multisyllabic('судија'))
        self.assertFalse(utils.is_multisyllabic('Зора'))
        self.assertFalse(utils.is_multisyllabic('Ана'))

    def test_maybe_insert_nepostojano_a(self):
        self.assertEqual('Небојаша', utils.maybe_insert_nepostojano_a('Небојша'))
        self.assertEqual('Ана', utils.maybe_insert_nepostojano_a('Ана'))
        self.assertEqual('судија', utils.maybe_insert_nepostojano_a('судија'))
        self.assertEqual('девојака', utils.maybe_insert_nepostojano_a('девојка'))

if __name__ == '__main__':
    unittest.main()
