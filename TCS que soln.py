from array import *
arr=[5,7,11,13]
result=[]
k=len(arr)
for i in range(k):
    for j in range(i):
        x=arr[i]-arr[j]
        if x==6:
            result.append(arr[i])
            result.append(arr[j])
        print(result)
