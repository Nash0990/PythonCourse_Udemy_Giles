#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 04:44:33 2020

@author: lifecell
"""

import timeit

import Functions_Test


t1=timeit.Timer("FibNum(100)","from Functions_Test import FibNum")
t2=timeit.Timer("fib2(10)","from Functions_Test import fib2")
print(t1.timeit(5))
print(t2.timeit(5))

