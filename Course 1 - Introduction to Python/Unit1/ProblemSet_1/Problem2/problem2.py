#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 00:08:55 2022

@author: juan
"""

s='wqboboovmcoofbobobfvbojbobb'

needle = 'bob'
count=sum(s[i:i+len(needle)] == needle for i in range(len(s)))

print("Number of times bob occurs is: "+ str(count))    



