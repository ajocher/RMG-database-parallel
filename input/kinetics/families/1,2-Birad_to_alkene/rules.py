#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Y_12birad",
    kinetics = ArrheniusEP(
        A = (1e+08, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 2,
    label = "Y_12_00",
    kinetics = ArrheniusEP(
        A = (1e+08, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 3,
    label = "Y_12_10",
    kinetics = ArrheniusEP(
        A = (6.31e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 4,
    label = "Y_12_20",
    kinetics = ArrheniusEP(
        A = (3.98e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 5,
    label = "Y_12_30",
    kinetics = ArrheniusEP(
        A = (2.51e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 6,
    label = "Y_12_40",
    kinetics = ArrheniusEP(
        A = (1.58e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 7,
    label = "Y_12_01",
    kinetics = ArrheniusEP(
        A = (5.01e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 8,
    label = "Y_12_02",
    kinetics = ArrheniusEP(
        A = (2.51e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 9,
    label = "Y_12_03",
    kinetics = ArrheniusEP(
        A = (1.26e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 10,
    label = "Y_12_04",
    kinetics = ArrheniusEP(
        A = (6.31e+06, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 11,
    label = "Y_12_11",
    kinetics = ArrheniusEP(
        A = (3.16e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 12,
    label = "Y_12_12",
    kinetics = ArrheniusEP(
        A = (1.58e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 13,
    label = "Y_12_21",
    kinetics = ArrheniusEP(
        A = (2e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 14,
    label = "Y_12_22",
    kinetics = ArrheniusEP(
        A = (1e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 15,
    label = "Y_12_13",
    kinetics = ArrheniusEP(
        A = (7.94e+06, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

entry(
    index = 16,
    label = "Y_12_31",
    kinetics = ArrheniusEP(
        A = (1.26e+07, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
)

