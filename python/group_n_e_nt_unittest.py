import definitions as defs
import group_n_e_nt as n_e_nt
import unittest


class TestGroupNENTInflection(unittest.TestCase):
    # уже
    def test_group_n_e_nt_normal(self):
        self.assertEqual(["време", "времена", "времену", "време", "време", "временом", "времену",
                          "времена", "времена", "временима", "времена", "времена", "временима", "временима"],
                         n_e_nt.inflect("време", {'plural': 'времена'}))
        self.assertEqual(["дугме", "дугмета", "дугмету", "дугме", "дугме", "дугметом", "дугмету",
                          "дугмета", "дугмета", "дугметима", "дугмета", "дугмета", "дугметима", "дугметима"],
                         n_e_nt.inflect("дугме", {'plural': 'дугмета'}))
        # Inflected using normal rules, without providing alternate plural form (a_plural, and its gender)
        self.assertEqual(["ждребе", "ждребета", "ждребету", "ждребе", "ждребе", "ждребетом", "ждребету",
                          "ждребета", "ждребета", "ждребетима", "ждребета", "ждребета", "ждребетима", "ждребетима"],
                         n_e_nt.inflect("ждребе", {'plural': 'ждребета'}))

    def test_group_n_e_nt_young_being(self):
        # Inflected using alternate plural form/rules.
        self.assertEqual(["ждребе", "ждребета", "ждребету", "ждребе", "ждребе", "ждребетом", "ждребету",
                          "ждребад", "ждребади", "ждребадима", "ждребади", "ждребади", "ждребадима", "ждребадима"],
                         n_e_nt.inflect("ждребе", {'plural': 'ждребета', 'a_plural': 'ждребад', 'a_p_gender': defs.Gender.F}))

    def test_get_extra_nt(self):
        self.assertEqual('н', n_e_nt.get_extra_nt("време", 'времена'))
        self.assertEqual('т', n_e_nt.get_extra_nt("дугме", 'дугмета'))


if __name__ == '__main__':
    unittest.main()
