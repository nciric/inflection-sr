import inflection_sr as inflect
import unittest


class TestClassification(unittest.TestCase):

    def test_group_f_c(self):
        self.assertEqual(inflect.DeclinationGroup.GROUP_F_C,
                         inflect.classify_noun("ствар", "ствари", inflect.Gender.F))

    def test_group_mfn_a(self):
        self.assertEqual(inflect.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("жена", "жене", inflect.Gender.F))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("судија", "судије", inflect.Gender.M))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("доба", "доба", inflect.Gender.N))

    def test_group_n_e_nt(self):
        self.assertEqual(inflect.DeclinationGroup.GROUP_N_E_NT,
                         inflect.classify_noun("име", "имена", inflect.Gender.N))
        self.assertEqual(inflect.DeclinationGroup.GROUP_N_E_NT,
                         inflect.classify_noun("дупе", "дупета", inflect.Gender.N))

    def test_group_mn_coe(self):
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("камен", "камена", inflect.Gender.M))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("Живко", "Живка", inflect.Gender.M))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("Павле", "Павла", inflect.Gender.M))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("село", "села", inflect.Gender.N))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("поље", "поља", inflect.Gender.N))

    def test_failed_to_classify(self):
        with self.assertRaises(ValueError):
            inflect.classify_noun("имеу", "имеуа", inflect.Gender.N)


if __name__ == '__main__':
    unittest.main()
