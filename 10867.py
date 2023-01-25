import sys
input = sys.stdin.readline

N=int(input())
a=list(input().split(" "))
a[-1]= a[-1].replace("\n","")
    
for i in range(0,N):
    for j in range(0,N-i-1):
        if (a[j]>a[j+1]):
            tmp=a[j+1]
            a[j+1]=a[j]
            a[j]=tmp
          
for i in range(N-1):
    if (a[i]!=a[i+1]):
        print(a[i],end=" ")
print(a[N-1])     