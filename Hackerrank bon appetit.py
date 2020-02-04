#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    c=0
    m=len(bill)
    for i in range(m):
        if(i!=k):
            c+=bill[i]
    e=c//2
    if(e==b):
        print("Bon Appetit")
    else:
        p=abs(e-b)
        print(p)    



if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
