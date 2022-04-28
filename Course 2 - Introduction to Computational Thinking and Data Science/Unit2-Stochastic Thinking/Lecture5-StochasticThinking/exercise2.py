# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:29:51 2022

@author: Juan Sebastian Velasquez Acevedo
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    
    randomEven = random.randrange(0,100,2)
    return randomEven
    

print(genEven())