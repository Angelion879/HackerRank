# Let's Review

import string
import sys

t = int(input())

for n in range(0,t,1):
    s = input()
    a = len(s)

    for n in range(0,a,1):
        if(n%2 == 0):
            sys.stdout.write(s[n])
        else:
            continue
    sys.stdout.write(" ")
    for n in range(0,a,1):
        if (n%2 != 0):
            sys.stdout.write(s[n])
        else:
            continue
    print()
