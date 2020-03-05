import group_f_c as f_c
import unittest


class TestGroupFCInflection(unittest.TestCase):

    def test_group_f_c_1(self):
        self.assertEqual(["ствар", "ствари", "ствари", "ствар", "ствари", "ствари", "ствари",
                          "ствари", "ствари", "стварима", "ствари", "ствари", "стварима", "стварима"],
                         f_c.inflect("ствар"))

    def test_group_f_c_2(self):
        self.assertEqual(["чађ", "чађи", "чађи", "чађ", "чађи", "чађи", "чађи",
                          "чађи", "чађи", "чађима", "чађи", "чађи", "чађима", "чађима"],
                         f_c.inflect("чађ"))

if __name__ == '__main__':
    unittest.main()
