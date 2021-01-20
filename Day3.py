# Intro to Conditional Statements

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    if (N % 2 == 0 and 2 < N < 5 or N % 2 == 0 and 20 < N):
        print("Not Weird")
    elif (N % 2 == 0 and 5 < N <= 20 or N % 2 != 0):
        print("Weird")
