#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:22:46 2020

@author: lifecell
"""
for i in range(10):
    print(i)
    
for i in range(10):
    print(i,end=" ")
    
for i in range(0,101,4):
    print(i)

for i in range(100,0,-1):
    print(i)
    
word="python"

for char in word:
    print(char)
    
    
x=6
x=x+1

x += 1


data=[10,20,30,40,50,60,70]
total=0
for num in data:
    total=total+num
print(total)

sum(data)    
maxnum=0
for num in data:
    if(maxnum<num):
        maxnum=num

print(maxnum)

max(data)


#Bubble Sort
#data=random.sample(range(1,100),10)
data=[24,99,64,12,0,90,1,10]
data_copy=data

for i in range(len(data_copy)):
    for j in range(0,len(data_copy)-i-1):
        if data_copy[j]>data_copy[j+1]:
            data_copy[j],data_copy[j+1]=data_copy[j+1],data_copy[j]

print(data)
print(data_copy)
sorted(data)

#While loop
n=10
while n>0:
    print(n)
    n-=1
    
    
#Usage
count=0
user_input=int(input("Please entre the age of each student, Once you are done, enter -1>>>"))
ages=[]

while user_input > 0:
    ages.append(user_input)
    user_input=int(input("The next age is >>"))

print("The ages are ",sorted(ages))