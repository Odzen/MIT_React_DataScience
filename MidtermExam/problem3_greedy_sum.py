# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:52:31 2022

@author: Juan Sebastian Velasquez
"""
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    remain = s
    for i in L:
        if i <= remain:
            mult = remain // i
            multipliers.append(mult)
            remain -= i * mult
        else:
            multipliers.append(0)
    sum1 = 0
    for j in range(len(multipliers)):
        sum1 += L[j]*multipliers[j]
    if sum1 == s:
        return sum(multipliers)
    else:
        return 'no solution'

