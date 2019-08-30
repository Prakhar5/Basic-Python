from array import *
ar=[]
k=int(input("array length"))
count=0
big = max(ar)
k=len(ar)
for i in range(k):
    if(ar[i]==big):
    count+=1

print(count)
