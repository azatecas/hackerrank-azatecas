#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mem = {}
    pairs = 0
    for item in ar:
        if item in mem:
           mem[item] = mem[item] + 1
        else:
            mem[item] = 1 
        if mem[item] % 2 == 0:
            pairs += 1
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
