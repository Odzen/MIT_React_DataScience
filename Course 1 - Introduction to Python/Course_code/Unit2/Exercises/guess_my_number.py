#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 00:36:43 2022

@author: juan
"""

number = int(input("Please think of a number between 0 and 100!"))
#epsilon=0
low = 0.0
high = 100
ans = (high+low)/2

answer_user=""

while  answer_user!= 'c':
    if(answer_user== 'h' or answer_user== 'l' or answer_user== 'c'):
        if answer_user== 'l':
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    else:
        print("Sorry, I did not understand your input.")
    print("Is your secret number "+str(ans)+"?")
    answer_user=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print("Game over. Your secret number was:"+str(ans))

#ans=50
#number=70
#50<50 - yes
#low = 50
#ans = (100 + 50) / 2 = 75

#75<70 - no
#hight=75
#ans=(75+50)/ 2 = 60

