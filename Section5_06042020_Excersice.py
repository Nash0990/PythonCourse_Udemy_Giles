#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 03:07:16 2020

@author: lifecell
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''

user_input=int(input("Please enter a number between 1 and 5\n>>>"))

if user_input==1:
    print("one")
elif user_input==2:
    print("two")
elif user_input==3:
    print("three")
elif user_input==4:
    print("four")
elif user_input==5:
    print("five")
else:
    print("Out of range!!!")
    
    
'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''

user_input=input("Please typein a number between one and five\n>>>")

user_input=user_input.lower()

if user_input=="one":
    print(1)
elif user_input=="two":
    print(2)
elif user_input=="three":
    print(3)
elif user_input=="four":
    print(4)
elif user_input=="five":
    print(5)
else:
    print("Out of range!!!")
    

'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''

num=5
user_input=input("I have a number in mind between 1 and 10, Can you guess it ?\n>>>")

if user_input.isdigit():
    user_input=int(user_input)
    if user_input==num:
        print("Yes!!!!, You guessed the number correctly as ",num)
    elif user_input<num and user_input>0:
        print("Wrong!!!!! The number you guessed is lesser than number.")
    elif user_input>num and user_input<11:
        print("Wrong!!!!! The number you guessed is bigger than number.")
    else:
        print("Number out of bounds")
else:
    print("Thats not even an integer")
    
    
'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''

name=input("Hey, whats your name ?\n>>>")
len_name=len(name)
if len_name<=5:
    print("Your name has ",len_name,"chars")
else:
    print("Length of your name is a secret.")


'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''

print("Please entre two numbers between 1 and 20\n")
num1=int(input("Number 1 : "))
num2=int(input("Number 2 : "))

if num1>15 and num2>15:
    print("The product of the two numbers is ",num1*num2)
elif num1>15 or num2>15:
    print("The sum of the two numbers is ",num1+num2)
else:
    print(0)


'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''

print("Please entre two numbers\n")
val1=int(input("Number 1 : "))
val2=int(input("Number 2 : "))

print("Entered numbers are val1=",val1," and val2=",val2,end="\n")

swap=val1
val1=val2
val2=swap
#Better way to do is
#val1,val2=val2,val1
print("Post swap val1=",val1," val2=",val2)