import os
import sys
import math

def number():
    """Calculates the numbers that the user inputs and then displays to the
terminal screen."""
    x = int(input("Num1:"))
    y = int(input("Num2:"))
    z = int(input("Num3:"))
    num = 5
    if num == x or y or z:
        print(f"[*] Type in the number that the user has to input.")

number()

def age():
    """Calculates the ages that the user inputs and then displays to the 
terminal screen."""
    x = int(input("Age1:"))
    y = int(input("Age2:"))
    z = int(input("Age3:"))
    age = 5
    if age == x or y or z:
        print(f"[*] Type in the age that the user has to input.")

    if age >= 18:
        print(f"You are {age} year old and a adult")
    else:
        print(f"You are {age} year old. Get a life and study hard.")
age()
