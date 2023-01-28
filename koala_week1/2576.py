odd=[]
for i in range(7):
    A=int(input())
    if (A%2==1):
        odd.append(A)

if len(odd)==0:
    print("-1")
else:
    print(sum(odd))
    print(min(odd))