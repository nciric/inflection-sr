""" Implements declination group 3. From documentation:
По трећој именичкој врсти мењају се именице које се у свом основном облику (номинативу једнине) завршавају на -а.
Образац промене исти је и за именице (природног) мушког и за именице женског рода.
"""

import definitions as defs
import utils

EXTENSIONS = ['а', 'е', 'и', 'у', 'о', 'ом', 'и',
              'е', 'а', 'ама', 'е', 'е', 'ама', 'ама']


def inflect(singular):
    """ Returns array of inflected forms, starting with nominative, singular."""
    is_multi = utils.is_multisyllabic(singular)
    alt_extensions = EXTENSIONS
    # Fixing vocative, singular exceptions.
    if is_country_exception(singular):
        pass
    elif singular.endswith('ица') and is_multi:
        alt_extensions[defs.Cases.S_VOCATIVE] = 'е'
    # Countries, made from adjective
    elif singular[0:1].isupper() and singular.endswith(('ска', 'чка', 'шка')):
        alt_extensions[defs.Cases.S_VOCATIVE] = 'а'
    # Proper name, multisyllabic or an exception.
    elif (singular[0:1].isupper() and is_multi) or is_exception(singular):
        alt_extensions[defs.Cases.S_VOCATIVE] = 'а'
    # Fixing genitive, plural exceptions.
    return [generate_case(singular, x, i) for (i, x) in enumerate(alt_extensions, 0)]


def generate_case(singular, extension, case):
    """ Generate proper form. In most cases it's plain concatenation,
        but there are exceptions."""
    # Chop of ending а character, we don't need it anymore.
    singular = singular[:-1]
    # From here on, only genitive plural is special.
    if case != defs.Cases.P_GENITIVE:
        return singular + extension

    if singular.endswith(('ст', 'шт', 'зд', 'шћ', 'жђ', 'шч', 'жџ', 'јш')):
        return singular + extension

    if singular.endswith(('тњ', 'дњ', 'пт', 'лб', 'рв')):
        return singular + 'и'

    # Case of "nepostojano a": devojka -> devoj_a_ka.
    singular = utils.maybe_insert_nepostojano_a(singular)

    return singular + extension


def is_country_exception(singular):
    """ Some countries inflect properly (so no exceptions), but fall into:
        multisyllabic, personal name case, so we need to make them exceptions."""
    EXCEPTIONS = ['Аустрија', 'Албанија', 'Аустралија', 'Ангола', 'Аргентина', 'Јерменија',
                  'Белорусија', 'Белгија', 'Боливија', 'Боцвана', 'Камбоџа', 'Канада', 'Костарика', 'Еритреја', 'Естонија',
                  'Етиопија', 'Гамбија', 'Грузија', 'Гренада', 'Гватемала', 'Гвинеја', 'Индија', 'Индонезија', 'Италија', 'Јамајка',
                  'Кенија', 'Кореја', 'Летонија', 'Либерија', 'Либија', 'Литванија', 'Малезија', 'Мауританија', 'Микронезија',
                  'Молдавија', 'Монголија', 'Намибија', 'Холандија', 'Никарагва', 'Нигерија', 'Македонија', 'Палестина',
                  'Панама', 'Португалија', 'Румунија', 'Русија', 'Руанда', 'Самоа', 'Србија', 'Словенија', 'Сомалија', 'Шпанија',
                  'Сирија', 'Танзанија', 'Уганда', 'Украјина', 'Венецуела', 'Замбија']
    return singular in EXCEPTIONS


def is_exception(singular):
    """ For many of these, the only change is vocative, singular that goes from o to a."""
    EXCEPTIONS = ['Бранка', 'Ана', 'Уна',
                  'мама', 'тата', 'баба', 'деда', 'стрина', 'тетка']
    return singular in EXCEPTIONS
