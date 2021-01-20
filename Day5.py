# Loops

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    i = 1
    while(i <= 10):
        res = n * i
        print(n, "x", i, "=", res)
        i += 1
