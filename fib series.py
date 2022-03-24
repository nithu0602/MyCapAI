# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:35:30 2022

@author: Nithyashri
"""

#Write a Python Program for Fibonacci numbers
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

f0=0
f1=1
f2=0
n=int(input("Enter the term"))

if(n<0):
    print("Error")

elif (n==1):
    print(f0)
    
elif (n==2):
    print(f1)
    
else:
    print(f0,end=" ")
    print(f1,end=" ")
    for i in range(3,n+1):
        f2=f0+f1
        print(f2,end=" ")
        f0=f1
        f1=f2