""" Implements declination group 2. From documentation:
По другој именичкој врсти мењају се именице средњег рода чији се основни облик завршава самогласником е, а чија се основа у зависним падежима,
сем у номинативу и вокативу једнине, проширује сугласницима н, т.
"""

import definitions as defs
import group_f_c as f_c

from collections import Counter as mset

EXTENSIONS = ['', 'а', 'у', '', '', 'ом', 'у',
              'а', 'а', 'има', 'а', 'а', 'има', 'има']


def inflect(singular, options):
    """ Returns array of inflected forms, starting with nominative, singular."""
    # Get inflection as is, without alternate forms.
    normal = [generate_case(singular, options, x) for x in EXTENSIONS]
    # Check if we have extra info required for alternate forms.
    a_plural = options.get('a_plural')
    a_p_gender = options.get('a_p_gender')
    if a_plural == None or a_p_gender == None:
      return normal

    if a_p_gender == defs.Gender.F:
      # Pretend our plural is singular for 4th group.
      # Also skip first returned result, since it won't match the pattern.
      group_f_c_result = f_c.inflect(a_plural)
      return normal[:7] + [a_plural] + group_f_c_result[8:]

    # For cases we didn't cover.
    return normal


def generate_case(singular, options, extension):
    """ Generate proper form. In most cases it's plain concatenation,
        except for nouns that represent young beings (see tests)."""
    if extension == '':
      return singular

    extra_nt = get_extra_nt(singular, options['plural'])
    return singular + extra_nt + extension


def get_extra_nt(singular, plural):
    """ Returns either n or t that has to be in plural."""
    difference = mset(plural) - mset(singular)
    if difference['н'] != 0:
      return 'н'
    else:
      return 'т'
