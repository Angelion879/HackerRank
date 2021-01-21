# Binary Numbers

import math
import os
import random
import re
import sys

def sequence (n):
    l = list(n)
    counter = 0
    check = 0
    for nu in range (0, len(l), 1):
        if l[nu] == '1':
            counter += 1
            counter2 = counter
        else:
            check = counter2
            counter = 0
    if counter2 > check:
        print(counter2)
    else:
        print(check)

if __name__ == '__main__':
    n = int(input())
    sequence(bin(n) [2: ])
