#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:17:05 2020

@author: lifecell
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
print("Please enter two numbers between 1 and 100")
num=[]
num.append(int(input("Enter first number\n>>>")))
num.append(int(input("Enter second number\n>>>")))
num=sorted(num)


for i in range(num[0],num[1]):
    print(i)
    
'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
name=input("Please enter a name or a string of char:")
namelen=len(name)
name_reverse=""
for char in range(1,namelen+1):
    print(name[-char])
    name_reverse=name_reverse+name[-char]
print(name_reverse)
    
'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''

num=int(input("Please enter a number for the times table:"))

for i in range(1,21):
    print(num," x ",i," = ",num*i )
    
'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''

for j in range(1,13):
    print("Times table for ",j)
    for i in range(1,21):
        print(j," x ",i," = ",j*i )
        
        
'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

num=input("Please start entering numbers one after another and enter any alphabet to stop>>>")
num_list=[]
#First we make sure and check if the input is a number or a alphabet
if num.isalpha():
    print("Please enter atleast one number!!")
else:
    while num.isdigit():
        num=int(num)
        num_list.append(num)
        num=input("Entre the next number>>")
    list_num=len(num_list)
    list_sum=sum(num_list)
    mean=list_sum/list_num
    print("The mean of the numbers inputed is ",mean)
    

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''

num=15
num_ori=num
out=1
#factorial of a number is basically product of n, n-1,n-2,...1. 
#So in the below while loop we are multiplying the num wth n-1 till we reach n=1.
while num > 0:
    out=out*num
    num=num-1

print(f"The factorial of {num_ori} is {out}")


'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
fib=[0,1]
while len(fib)<20:
    new=fib[len(fib)-1]+fib[len(fib)-2]
    fib.append(new)

print(fib)

'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
F_list=[5,1,4,1,1]
n="*"
for i in F_list:
    print(n*i)


'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
num_list=list(range(1,101))
odd=[]
even=[]
for i in num_list:
    if i==1:
        odd.append(i)
    elif i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(f"The Odd number below 100 are {odd}")
print(f"THe Even numbers below 100 are {even}")

