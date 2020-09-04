import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip=float(meal_cost*float(tip_percent/100))
    
    tax=float(meal_cost*float(tax_percent/100))
    
    tot=float(meal_cost+tip+tax)
    
    print(round(tot))
    

if __name__ == '__main__':
    meal_cost = float(input())
