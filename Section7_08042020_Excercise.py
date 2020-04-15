#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:17:45 2020

@author: lifecell
"""

capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
            }

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

user_input=input("Please enter the name of a country:\n>>")

if user_input in capitals:
    print(f"The capital of {user_input} is {capitals[user_input]}")
else:
    print(f"The country {user_input} is not in our dictionary")
    
    
'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
a=0
b=1
fib_dict={}
for i in range(1,13):
    fib_dict[i]=a
    a,b=b,a+b
    
'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
company=['Python DS','PythonSoft','Pythazon','Pybook']
status=['open','high','low','close']
share=[[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]

company_dict={}
for i in range(0,4):
    status_dict={}
    for j in range(0,4):
        status_dict[status[j]]=share[j][i]
    company_dict[company[i]]=status_dict
    
#Alternate solution
company_dict=dict()
for i in range(len(status)):
    company_dict[company[i]]=dict(zip(status,share[i]))

    
'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''
# Days until holiday!
import datetime

today = datetime.date.today()

print(f"Today's date is {today}")
holiday = datetime.date(2020,12,25)
delta = holiday - today

print(f"Just {delta.days} days until the holidays!")

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
import random
from matplotlib import pyplot as plt
Alpha_dict={}
for i in range(97,123):
    Alpha_dict[chr(i).upper()]=random.random()
plt.bar(Alpha_dict.keys(),Alpha_dict.values())

'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
['Diamonds','Spades','Clubs','Hearts']
'''

suits=['Diamonds','Spades','Clubs','Hearts']
cards=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
pack_dict={}

for i in suits:
    pack_dict[i]=cards

