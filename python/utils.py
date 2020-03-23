""" Helful methods, like finding multisyllabic words etc."""

import definitions as defs
import re

from collections import Counter as mset


def ends_with_consonant(noun):
    """ Returns true if string ends with consonant. """
    return not noun.endswith(defs.VOWELS)


def has_extra_nt(singular, plural):
    """ Returns true if non-nominative forms add n or t. """
    difference = mset(plural) - mset(singular)
    return difference['н'] != 0 or difference['т'] != 0


def is_multisyllabic(word):
    """ Returns true if word has 3 or more vowels, otherwise returns false.
        For example Zora is 2-syllabic (False), Nebojsa is 3-syllabic (True).
    """
    multiset = mset(word)
    sum = 0
    for vowel in defs.VOWELS:
        sum += multiset[vowel]
    if sum >= 3:
        return True
    return False


def maybe_insert_nepostojano_a(word):
    """ Inserts 'a' in between two ending consonants."""
    return re.sub(r'^(.*?)([^аеиоу][^аеиоу])([аеиоу]?)$', insert_a, word, flags = re.IGNORECASE)


def insert_a(group_match):
    """ Inserts letter a between two characters in middle group."""
    match = group_match.group(2)
    return group_match.group(1) + match[:1] + 'а' + match[1:] + group_match.group(3)