""" Implements declination group 4. From documentation:
Именице женског рода које се у номинативу једнине завршавају наставком -∅ (тј. имају видљив сугласнички завршетак) мењају се по четвртој именичкој врсти.
"""

import definitions as defs

EXTENSIONS = ['', 'и', 'и', '', 'ју', 'и', 'и',
              'и', 'и', 'има', 'и', 'и', 'има', 'има']

# Јотовање
J_TRANSITION = {'д': 'ђ', 'т': 'ћ', 'л': 'љ', 'н': 'њ', 'з': 'ж', 'с': 'ш'}

PBMV_TRANSITION = ('п', 'б', 'м', 'в')

# Једначење сугласника по месту творбе
ZS_TRANSITION = {'с': 'ш', 'з': 'ж'}


def inflect(singular):
    """ Returns array of inflected forms, starting with nominative, singular."""
    return [generate_case(singular, x, i) for (i, x) in enumerate(EXTENSIONS, 0)]


def generate_case(singular, extension, case):
    """ Generate proper form. In most cases it's plain concatenation,
        except for vocative, singular."""
    if case != defs.Cases.S_VOCATIVE:
        return singular + extension

    # Јотовање
    # Ненепчани сугласници испред гласа Ј прелазе у непчане: Д у Ђ, Т у Ћ, Л у Љ, Н у Њ, З у Ж, С у Ш.
    if singular.endswith(tuple(J_TRANSITION.keys())):
        head = singular[:-1]
        endswith = singular[-1:]
        # We are not done here. If head ends with з or с, they change into ж, ш.
        # Example is младост into младо-шћ-у.
        if head.endswith(tuple(ZS_TRANSITION.keys())):
            new_head = head[:-1]
            new_endswith = head[-1:]
            head = new_head + ZS_TRANSITION[new_endswith]
        return head + J_TRANSITION[endswith] + 'у'

    # Непчани: Ђ, Ћ, Љ, Њ, Ж, Ш само добијају у.
    if singular.endswith(tuple(J_TRANSITION.values())):
        return singular + 'у'

    # Уснени сугласници П, Б и М и зубноуснени сугласник В, испред самогласника Ј, прелазе у групе ПЉ, БЉ, МЉ и ВЉ.
    if singular.endswith(PBMV_TRANSITION):
        return singular + 'љу'

    # And everything else will get the ју extension.
    return singular + extension
