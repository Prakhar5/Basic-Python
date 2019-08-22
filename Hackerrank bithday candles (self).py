from array import *
arr=[]
n=int(input("array length"))

for i in range(n):
    x = (input()) 
    arr.append(x)
    continue
print(arr)
count=0
for j in range(n):
    if arr[i]==arr[j-i]:
        count+=1
print(count)
