#!/bin/python3
from collections import Counter 
import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict1 = Counter(a) 
    dict2 = Counter(b) 
    
    commonDict = dict1 & dict2 

    ls=list(commonDict.elements())

    return ((len(a)-len(ls))+len(b)-len(ls))

if __name__ == '__main__':
    
    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)
