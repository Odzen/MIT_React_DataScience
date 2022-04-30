# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:44:03 2022

@author: Juan Sebastian Velasquez
"""

def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    
    coefficients = [0,0,0,0]
    
    
    multipliers = [1, 5, 10 ,25]
    
    
    if s == 0:
        return coefficients
    
    remainder = s
    while remainder > 0:
        if remainder < 5 : 
            coefficients[0] += 1
            remainder -= multipliers[0]
        elif remainder < 10 : 
            coefficients[1] += 1
            remainder -= multipliers[1]
        elif remainder < 25 : 
            coefficients[2] += 1
            remainder -= multipliers[2]
        else:
            coefficients[3] += 1
            remainder -= multipliers[3]
    
    sum1 = 0
    inversedMultipliers = multipliers[::-1]
    inversedCoefficients = coefficients[::-1]
    for i in range(len(inversedCoefficients)):
        sum1 += inversedCoefficients[i] * inversedMultipliers[i]
    
    #return coefficients
    if sum1 == s:
        return inversedCoefficients
    else:
        return None

#print(solve(100))