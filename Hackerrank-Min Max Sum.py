from array import *
from math import *
import numpy as np
arr=[]
n=int(input("Enter the length of array"))
for i in range(n):
    x=int(input("Enter the next value"))
    arr.append(x)




sum2=[]
j=len(arr)
sum=0;
for i in range(j):
    sum=sum+arr[i]
for i in range(j):
    sum1=sum-arr[i]
    sum2.append(sum1)
print(sum2)
print(max(sum2))
print(min(sum2))