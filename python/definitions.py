""" Common definitiont used across codebase."""

from enum import Enum
from enum import IntEnum

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


class Cases(IntEnum):
    """ Indexing into extensions lists. """
    S_NOMINATIVE = 0
    S_GENITIVE = 1
    S_DATIVE = 2
    S_ACCUSATIVE = 3
    S_VOCATIVE = 4
    S_INSTRUMENTAL = 5
    S_LOCATIVE = 6
    P_NOMINATIVE = 7
    P_GENITIVE = 8
    P_DATIVE = 9
    P_ACCUSATIVE = 10
    P_VOCATIVE = 11
    P_INSTRUMENTAL = 12
    P_LOCATIVE = 13