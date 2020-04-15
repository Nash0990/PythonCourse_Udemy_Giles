#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 04:47:12 2020

@author: lifecell
"""

def hello():
    print("Hello World!!")    

def hi(name):
    print(f"Hello {name}!!!")

def hi2(name='Nahush'):
    print(f"Hello {name}!!!")

def FibNum(num=20):
    '''Calculates and returns the fibonacci series from 1 to num'''
    out=[]
    a=0
    b=1
    for i in range(1,num+1):
        out.append(a)
        a,b=b,a+b
    return out

def calcMean(first,*remainder):
    mean=(first+sum(remainder))/(1+len(remainder))
    return mean

def fib2(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)
