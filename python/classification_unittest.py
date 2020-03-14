import inflection_sr as inflect
import unittest


class TestClassification(unittest.TestCase):

    def test_group_f_c(self):
        self.assertEqual(inflect.DeclinationGroup.GROUP_F_C,
                         inflect.classify_noun("ствар", {'plural': "ствари", 'gender': inflect.Gender.F}))

    def test_group_mfn_a(self):
        self.assertEqual(inflect.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("жена", {'plural': "жене", 'gender': inflect.Gender.F}))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("судија", {'plural': "судије", 'gender': inflect.Gender.M}))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("доба", {'plural': "доба", 'gender': inflect.Gender.N}))

    def test_group_n_e_nt(self):
        self.assertEqual(inflect.DeclinationGroup.GROUP_N_E_NT,
                         inflect.classify_noun("име", {'plural': "имена", 'gender': inflect.Gender.N}))
        self.assertEqual(inflect.DeclinationGroup.GROUP_N_E_NT,
                         inflect.classify_noun("дупе", {'plural': "дупета", 'gender': inflect.Gender.N}))

    def test_group_mn_coe(self):
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("камен", {'plural': "камена", 'gender': inflect.Gender.M}))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("Живко", {'plural': "Живка", 'gender': inflect.Gender.M}))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("Павле", {'plural': "Павла", 'gender': inflect.Gender.M}))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("село", {'plural': "села", 'gender': inflect.Gender.N}))
        self.assertEqual(inflect.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("поље", {'plural': "поља", 'gender': inflect.Gender.N}))

    def test_failed_to_classify(self):
        with self.assertRaises(ValueError):
            inflect.classify_noun("имеу", {'plural': "имеуа", 'gender': inflect.Gender.N})


if __name__ == '__main__':
    unittest.main()
