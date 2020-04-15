#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:10:57 2020

@author: lifecell
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''

class BankAccount(object):
    '''
    Attributes
    ----------
    name: Account holder name
    accno: Account Number
    balance: Balance in the account
    '''
    
    def __init__(self,name,accno,balance=0.0):
        self.name=name
        self.accno=accno
        self.balance=balance
    
    def CheckBal(self):
        print(f'Account Holder:{self.name}\nAccount Number:{self.accno}\nBalance:{self.balance}')
    
    def deposit(self):
        credit=int(input('Please entre the amount of money you want to deposit:'))
        self.balance=self.balance+credit
        print(f'\nThe amount {credit} rupees ha been credit to you account and your updated balance is {self.balance}.')
    
    def withdraw(self):
        debit=int(input('Please entre the amount of money you want to withdraw:'))
        if self.balance<debit:
            print(f'Sorry you are trying to withdraw more money than you have.')
        else:
            self.balance=self.balance-debit
            print(f'You have succesfully withdrawn {debit} rupess and your updated balance is {self.balance} rupees.')

NahushAcc=BankAccount('Nahush',1224,5000)
NahushAcc.CheckBal()
NahushAcc.deposit()
NahushAcc.withdraw()


'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''
import math
class Circle(object):
    '''
    radius: Radius of the circle
    '''
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        area=(self.radius)**2 * math.pi
        return area

