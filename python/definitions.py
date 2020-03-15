""" Common definitiont used across codebase."""

from enum import Enum

VOWELS = ('а', 'е', 'и', 'о', 'у')


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
