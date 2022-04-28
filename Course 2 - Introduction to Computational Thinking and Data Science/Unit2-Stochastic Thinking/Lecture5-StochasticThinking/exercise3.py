# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:23:55 2022

@author: Juan Sebastian Velasquez Acevedo
"""

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    number = 10
    return number

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    number = random.randrange(10,22,2) #-- Stochastic
    return number

print(deterministicNumber())
print(stochasticNumber())