"""
Library that inflects given noun in Serbian language into all of its forms.
TODO(nciric): accept a CSV file for bulk operations.
Required inputs are: singular and plural in nominative, gender.
"""

from collections import Counter as mset
from enum import Enum

VOWELS = ("а", "е", "и", "о", "у")


class Gender(Enum):
    """ Gramatical gender """
    M = 1
    F = 2
    N = 3


class DeclinationGroup(Enum):
    """ Declination group noun belongs to. """
    # m, ending in consonant, -о and -е
    # n, ending in -о and -е, and where stem stays the same
    GROUP_MN_COE = 1
    # n, ending in -е and stem gains n or t in all cases except nominative
    GROUP_N_E_NT = 2
    # any gender, ending in -а
    GROUP_MFN_A = 3
    # f, ending in consonant (and associated adjective is female - we ignore this)
    GROUP_F_C = 4


def inflect_noun(singular, plural, gender: Gender):
    """ Takes singular, plural and gender of the noun.
        Returns an array with cases in singular followed by plural.
    """
    try:
      group = classify_noun(singular, plural, gender)
      if group == DeclinationGroup.GROUP_MN_COE:
        print("MN_COE")
      elif group == DeclinationGroup.GROUP_N_E_NT:
        print("N_E_NT")
      elif group == DeclinationGroup.GROUP_MFN_A:
        print("MFN_A")
      else:
        print("F_C")
    except:
      # Let caller decide whether to bail or to continue.
      raise
    return 0


def classify_noun(singular, plural, gender: Gender):
    """ Classifies noun into one of the four declination groups. """
    if gender == Gender.F and ends_with_consonant(singular):
        return DeclinationGroup.GROUP_F_C

    if singular.endswith("а"):
        return DeclinationGroup.GROUP_MFN_A

    if gender == Gender.N and singular.endswith("е") and has_extra_nt(singular, plural):
        return DeclinationGroup.GROUP_N_E_NT

    if (gender == Gender.M and ends_with_consonant(singular)) or \
       (gender in [Gender.N, Gender.M] and (singular.endswith("о") or singular.endswith("е"))):
        return DeclinationGroup.GROUP_MN_COE

    raise ValueError("Unknown noun declination group.",
                     singular, plural, gender)


def ends_with_consonant(noun):
    """ Returns true if string ends with consonant. """
    return not noun.endswith(VOWELS)


def has_extra_nt(singular, plural):
    """ Returns true if non-nominative forms add n or t. """
    difference = mset(plural) - mset(singular)
    return difference["н"] != 0 or difference["т"] != 0
