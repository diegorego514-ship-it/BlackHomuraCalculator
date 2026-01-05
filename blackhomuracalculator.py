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
