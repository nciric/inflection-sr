""" Implements declination group 4. From documentation:
Именице женског рода које се у номинативу једнине завршавају наставком -∅ (тј. имају видљив сугласнички завршетак) мењају се по четвртој именичкој врсти.
TODO(nciric): Having an adjective in front changes declination rules in some cases. Handle that case.
"""

EXTENSIONS = ["", "и", "и", "", "и", "и", "и",
              "и", "и", "има", "и", "и", "има", "има"]


def inflect(singular):
    """ Returns array of inflected forms, starting with nominative, singular."""
    return [singular + x for x in EXTENSIONS]
