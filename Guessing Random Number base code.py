import random
n=random.randint(0,20)

for i in range(1,5):
    x=int(input())
    print("Attempts used",i)
    if x==n:
        print("Good")
    else:
        print("Not good")
