"""
Library that inflects given noun in Serbian language into all of its forms.
Required inputs are: singular and plural in nominative, gender.
"""

import definitions as defs
import group_f_c
import group_mfn_a
import group_n_e_nt
import exceptions
import utils


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
            return group_mfn_a.inflect(singular)
        else:
            return group_f_c.inflect(singular)
    except:
        # Let caller decide whether to bail or to continue.
        raise


def classify_noun(singular, options):
    """ Classifies noun into one of the four declination groups. """
    if options['s_gender'] == defs.Gender.F and utils.ends_with_consonant(singular):
        return defs.DeclinationGroup.GROUP_F_C

    if singular.endswith('а'):
        return defs.DeclinationGroup.GROUP_MFN_A

    if options['s_gender'] == defs.Gender.N and singular.endswith('е') \
            and utils.has_extra_nt(singular, options['plural']):
        return defs.DeclinationGroup.GROUP_N_E_NT

    if (options['s_gender'] == defs.Gender.M and utils.ends_with_consonant(singular)) or \
       (options['s_gender'] in [defs.Gender.N, defs.Gender.M] and (singular.endswith(('о', 'е')))):
        return defs.DeclinationGroup.GROUP_MN_COE

    raise ValueError("Unknown noun declination group.",
                     singular, options)
