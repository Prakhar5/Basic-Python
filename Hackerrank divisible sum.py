#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    arr1=[]
    m=len(ar)
    for i in range(m):
        for j in range(i+1,m):
            l=(ar[i]+ar[j])
            p=(ar[i],ar[j])
            if(l%k==0):
                arr1.append(p)
    j=len(arr1)
    return j
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
