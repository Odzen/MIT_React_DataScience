# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:43:29 2022

@author: Juan Sebastian Velasquez
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    n = 0
    while True:
        if test(n) == True:
            return n
        elif test(-n) == True:
            return -n
        n += 1