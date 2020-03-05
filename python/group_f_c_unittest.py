import group_f_c as f_c
import unittest


class TestGroupFCInflection(unittest.TestCase):

    def test_group_f_c_thing(self):
        self.assertEqual(["ствар", "ствари", "ствари", "ствар", "ствари", "ствари", "ствари",
                          "ствари", "ствари", "стварима", "ствари", "ствари", "стварима", "стварима"],
                         f_c.inflect("ствар"))


if __name__ == '__main__':
    unittest.main()
