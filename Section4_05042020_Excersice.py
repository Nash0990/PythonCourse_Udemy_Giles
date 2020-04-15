#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 03:39:37 2020

@author: lifecell
"""

#Ask user for the radius and give the area of the circle with given radius.

pi=3.14159
radius=float(input("Please enter the radius of the cirlce of interest in cms: \n>>>"))

area=pi*radius**2

print("The area of the circle of interest is ",area,"sqcm",sep="")

#Ask user for the temperature in farenhite and output the temperature in Celcius

far=float(input("Please enter the temperature in Farhenite:\n>>"))
cel=(far-31) * 5/9
print("You entered temperature as ",far," Farenhite and that is ",cel,"` Celcius")

#Ask user for the 2 numbers and return the product

input1=int(input("Please entre a number 1 to multiply:\n>>>"))
input2=int(input("Please entre a number 2 to multiply:\n>>>"))

print("Product of the 2 numbers entered is ",input1*input2)

# 5 Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat
# 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
# What is the minimum number of pizzas needed - Use floor division

slicesNeeded=4*4
MinNumPizza=(slicesNeeded+5)//6
SlicesLeft=MinNumPizza*6-slicesNeeded
print("Minimum number of pizzas needed would be ",MinNumPizza," and there would be ",SlicesLeft," slices left.")
