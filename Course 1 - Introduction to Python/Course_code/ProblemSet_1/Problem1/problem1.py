#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 23:55:41 2022

@author: juan
"""

s= 'azcbobobegghakl'
vowels=0

for letter in s:
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' :
        vowels+=1

print("Number of vowels: " + str(vowels))