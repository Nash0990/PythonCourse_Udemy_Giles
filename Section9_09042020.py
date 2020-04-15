#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:10:03 2020

@author: lifecell
"""

x = 1
help(x)

y=[1,2,3]
help(y)
dir(y)
y.append(4)

z = {'a':1}
help(z)


#class Patient(object):
#    '''Medical centre patient'''
#    pass
#
#
#class Patient(object):
#    '''Medical centre patient'''
#    status='patient'
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    pass
#
#steven=Patient('Steven Huges',48)
#abigale=Patient('Abigale Potter',38)
#
#
#class Patient(object):
#    '''Medical centre patient'''
#    status='patient'
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    
#    def get_status(self):
#        print(f"Patient record {self.name}:{self.age} years.")
#
#steven=Patient('Steven Huges',48)
#abigale=Patient('Abigale Potter',38)


class Patient(object):
    '''
    Medical centre patient object
    Attributes
    ----------
    name: Patient name
    age: Patient age
    conditions: Existing medical conditions.
    '''
    
    status='patient'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.conditions=[]
    
    def get_details(self):
        print(f"Patient record {self.name}:{self.age} years.\nCurrent information :{self.conditions}")
    
    def add_info(self,information):
        self.conditions.append(information)


#steven=Patient('Steven Huges',48)
#abigale=Patient('Abigale Potter',38)

class Infant(Patient):
    '''Patient who are below 2 year old'''
    
    def __init__(self,name,age):
        self.vaccinations = []
        super().__init__(name,age)
    
    def add_vac(self,vaccine):
        self.vaccinations.append(vaccine)
    
    def get_details(self):
        print(f'Patient record {self.name}:{self.age} years.\nPatient has had {self.vaccinations} vaccines.\nCurrent information:{self.conditions}\n{self.name} IS AN INFANT AND HAS HE HAD ALL HIS/HER CHECKS?')

archie = Infant("Archie Fittlenorth",0)
archie.add_vac('MMR') 