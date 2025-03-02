# coding: utf8
from __future__ import unicode_literals

# TT: commented out
# I see no point in this type of lexical normalization
# currently considering for Ekavian-Jekavian normalization

_exc = {
    # Slang
    #"ћале": "отац",
    #"кева": "мајка",
    #"смор": "досада",
    #"кец": "јединица",
    #"тебра": "брат",
    #"штребер": "ученик",
    #"факс": "факултет",
    #"профа": "професор",
    #"бус": "аутобус",
    #"пискарало": "службеник",
    #"бакутанер": "бака",
    #"џибер": "простак",
}


NORM_EXCEPTIONS = {}

for string, norm in _exc.items():
    NORM_EXCEPTIONS[string] = norm
    NORM_EXCEPTIONS[string.title()] = norm
