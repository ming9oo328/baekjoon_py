N,K=map(int,input().split())
a=list(map(int,input().split(',')))
for j in range(K):
    b=[]
    for i in range(len(a)-1):
        b.append(a[i+1]-a[i])
    a=b
print(*a,sep=',')