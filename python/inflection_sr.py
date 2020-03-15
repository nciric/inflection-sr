"""
Library that inflects given noun in Serbian language into all of its forms.
Required inputs are: singular and plural in nominative, gender.
"""

import definitions as defs
import group_f_c
import group_n_e_nt
import exceptions

from collections import Counter as mset

def inflect_noun(singular, options):
    """ Takes singular nominative of the noun and additional options.
        Returns an array with cases in singular followed by plural.
    """
    try:
        # Try exceptions list first.
        result = exceptions.return_exception(singular)
        if result != None:
            return result
        # Otherwise try to classify noun type and call appropriate handler.
        group = classify_noun(singular, options)
        if group == defs.DeclinationGroup.GROUP_MN_COE:
            print('MN_COE')
        elif group == defs.DeclinationGroup.GROUP_N_E_NT:
            return group_n_e_nt.inflect(singular, options)
        elif group == defs.DeclinationGroup.GROUP_MFN_A:
            print('MFN_A')
        else:
            return group_f_c.inflect(singular)
    except:
        # Let caller decide whether to bail or to continue.
        raise


def classify_noun(singular, options):
    """ Classifies noun into one of the four declination groups. """
    if options['s_gender'] == defs.Gender.F and ends_with_consonant(singular):
        return defs.DeclinationGroup.GROUP_F_C

    if singular.endswith('а'):
        return defs.DeclinationGroup.GROUP_MFN_A

    if options['s_gender'] == defs.Gender.N and singular.endswith('е') \
            and has_extra_nt(singular, options['plural']):
        return defs.DeclinationGroup.GROUP_N_E_NT

    if (options['s_gender'] == defs.Gender.M and ends_with_consonant(singular)) or \
       (options['s_gender'] in [defs.Gender.N, defs.Gender.M] and (singular.endswith(('о', 'е')))):
        return defs.DeclinationGroup.GROUP_MN_COE

    raise ValueError("Unknown noun declination group.",
                     singular, options)


def ends_with_consonant(noun):
    """ Returns true if string ends with consonant. """
    return not noun.endswith(defs.VOWELS)


def has_extra_nt(singular, plural):
    """ Returns true if non-nominative forms add n or t. """
    difference = mset(plural) - mset(singular)
    return difference['н'] != 0 or difference['т'] != 0
