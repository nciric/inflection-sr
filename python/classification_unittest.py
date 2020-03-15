import definitions as defs
import inflection_sr as inflect
import unittest


class TestClassification(unittest.TestCase):

    def test_group_f_c(self):
        self.assertEqual(defs.DeclinationGroup.GROUP_F_C,
                         inflect.classify_noun("ствар", {'plural': "ствари", 's_gender': defs.Gender.F}))

    def test_group_mfn_a(self):
        self.assertEqual(defs.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("жена", {'plural': "жене", 's_gender': defs.Gender.F}))
        self.assertEqual(defs.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("судија", {'plural': "судије", 's_gender': defs.Gender.M}))
        self.assertEqual(defs.DeclinationGroup.GROUP_MFN_A,
                         inflect.classify_noun("доба", {'plural': "доба", 's_gender': defs.Gender.N}))

    def test_group_n_e_nt(self):
        self.assertEqual(defs.DeclinationGroup.GROUP_N_E_NT,
                         inflect.classify_noun("име", {'plural': "имена", 's_gender': defs.Gender.N}))
        self.assertEqual(defs.DeclinationGroup.GROUP_N_E_NT,
                         inflect.classify_noun("дупе", {'plural': "дупета", 's_gender': defs.Gender.N}))

    def test_group_mn_coe(self):
        self.assertEqual(defs.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("камен", {'plural': "камена", 's_gender': defs.Gender.M}))
        self.assertEqual(defs.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("Живко", {'plural': "Живка", 's_gender': defs.Gender.M}))
        self.assertEqual(defs.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("Павле", {'plural': "Павла", 's_gender': defs.Gender.M}))
        self.assertEqual(defs.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("село", {'plural': "села", 's_gender': defs.Gender.N}))
        self.assertEqual(defs.DeclinationGroup.GROUP_MN_COE,
                         inflect.classify_noun("поље", {'plural': "поља", 's_gender': defs.Gender.N}))

    def test_failed_to_classify(self):
        with self.assertRaises(ValueError):
            inflect.classify_noun("имеу", {'plural': "имеуа", 's_gender': defs.Gender.N})


if __name__ == '__main__':
    unittest.main()
