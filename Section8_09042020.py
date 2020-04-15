#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 03:01:48 2020

@author: lifecell
"""

#Files and Functions

f = open("kipling.txt",'w')
print(type(f))

f.write('We are now going to start writing into this file using python write function.\n\n')
f.write('If you can keep your head while all about you \nare losing theirs\
and blaming it on you,\n')

f.write('If you can trust yourself when all men doubt you,\n\
But make allowance for their doubting too;\n')

f.write('If you can wait and not be tired by waiting,\n\
Or being lied about, don\'t deal in lies,\n')

f.write('Or being hated, don\'t give way to hating,\n\
And yet don\'t look too good, nor talk too wise:\n')

f.close()

f=open("kipling.txt",'r')

print(f.read())

f.close()

f=open("kipling.txt",'r')

content=print(f.readlines())
#print(f.readline())

f.close()


f=open("kipling.txt",'a')
f.write('If you can dream - and not make dreams your master;\n\
If you can think - and not make thoughts your aim;\n')
f.close()


with open('kipling.txt','r') as f:
    for line in f.readline:
        print(line)




#Functions

def hello():
    print("Hello World!!")    

hello()

def hi(name):
    print(f"Hello {name}!!!")

hi("Nahush")

def hi2(name='Nahush'):
    print(f"Hello {name}!!!")

hi2("Manjari")

def FibNum(num=20):
    '''Calculates and returns the fibonacci series from 1 to num'''
    out=[]
    a=0
    b=1
    for i in range(1,num+1):
        out.append(a)
        a,b=b,a+b
    return out

FibNum(10)

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

def add_n_prod(n,j):
    add_o=n+j
    prod_o=n*j
    return add_o,prod_o

out=add_n_prod(2,5)
out_sum,out_prod=add_n_prod(2,5)



