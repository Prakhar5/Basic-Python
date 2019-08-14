from array import *
prime=[]
x,y=input("ENTER").split()

x=int(x)
y=int(y)

for val in range(x, y + 1):


   if val > 1:
       for n in range(2, val):
           if (val % n) == 0:
               break
       else:

           prime.append(val)

result=[]
k=len(prime)
count=0
for i in range(k):
    for j in range(i):
        x=prime[i]-prime[j]
        if x==6:
            result.append(prime[i])
            result.append(prime[j])
            count+=1
            print("Pair found (",prime[i],",",prime[j],")",end="")

print()
print(count)

