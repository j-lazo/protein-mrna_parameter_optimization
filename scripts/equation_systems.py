#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:59:57 2018

@author: jl
"""
import numpy as np


def gen_network_1(t, x, c):

    """
    Equation system proposed, without considering the interaction with md

    :param t: time parameter
    :param x: variables (list)
    :param c: constants (list)
    :return: solution of the system (list)
    """

    # variables

    mA = x[0]
    pA = x[1]
    mB = x[2]
    pB = x[3]
    mC = x[4]
    pC = x[5]

    # constants
    oxA = c[0]
    tA = c[1]
    kAC = c[2]
    nuAC = c[3]
    dmA = c[4]
    uA = c[5]
    dpA = c[6]
    oxB = c[7]
    tB = c[8]
    dmB = c[9]
    oxC = c[10]
    tC = c[11]
    kCB = c[12]
    nuCB = c[13]
    nuCA = c[14]
    nuAB = c[15]
    dmC = c[16]
    uC = c[17]
    dpC = c[18]
    kBA = c[19]
    uB = c[20]
    dpB = c[21]
    dpBC = c[22]
    kBC = c[23]
    
    dmadt = oxA*tA/(1+np.power((pC/kAC), nuAC))-dmA*mA
    dpadt = uA*mA-dpA*pA
    dmbdt = oxB*tB*(np.power(pA, nuAB))/(np.power(kBA, nuAB)+np.power(pA, nuAB))-dmB*mB
    dpbdt = uB*mB-(dpB+(dpBC*pC/(kBC+pC)))*pB
    dmcdt = oxC*tC*np.power((pB/kCB), nuCB)/(1+np.power((pB/kCB), nuCB)+np.power((pA/kBA), nuCA))-dmC*mC
    dpcdt = uC*mC-dpC*pC

    return [dmadt, dpadt, dmbdt, dpbdt, dmcdt, dpcdt]


def gen_network_2(t, x, c):

    """
    Equation system proposed,  considering the interaction with md
    :param t: time parameter
    :param x: variables (list)
    :param c: constants (list)
    :return: solution of the system (list)
    """

    # variables
    mA = x[0]
    pA = x[1]
    mB = x[2]
    pB = x[3]
    mC = x[4]
    pC = x[5]
    mD = x[6]


    # constants
    oxA = c[0]
    tA = c[1]
    kAC = c[2]
    nuAC = c[3]
    dmA = c[4]
    uA = c[5]
    dpA = c[6]
    oxB = c[7]
    tB = c[8]
    dmB = c[9]
    oxC = c[10]
    tC = c[11]
    kCB = c[12]
    nuCB = c[13]
    nuCA = c[14]
    nuAB = c[15]
    dmC = c[16]
    uC = c[17]
    dpC = c[18]
    kBA = c[19]
    uB = c[20]
    dpB = c[21]
    dpBC = c[22]
    kBC = c[23]
    oxD = c[24]
    tD = c[25]
    pX = c[26]
    dmD = c[27]
    kDB = c[28]
    nuDB = c[29]
    kDA = c[30]
    nuDA = c[31]
    kDC = c[32]
    nuDC = c[33]
    
    dmadt = oxA*tA/(1+np.power((pC/kAC), nuAC))-dmA*mA
    dpadt = uA*mA-dpA*pA
    dmbdt = oxB*tB*(np.power(pA, nuAB))/(np.power(kBA, nuAB)+np.power(pA, nuAB))-dmB*mB
    dpbdt = uB*mB-(dpB+(dpBC*pC/(kBC+pC)))*pB
    dmcdt = oxC*tC*np.power((pB/kCB), nuCB)/(1+np.power((pB/kCB), nuCB)+np.power((pA/kBA), nuCA))-dmC*mC
    dpcdt = uC*mC-dpC*pC
    dmdt = oxD*tD*np.power((pA/kDA), nuDA)/(1+np.power((pB/kDB), nuDB)+np.power((pC/kDC), nuDC))-dmD*mD

    return [dmadt, dpadt, dmbdt, dpbdt, dmcdt, dpcdt, dmdt]
