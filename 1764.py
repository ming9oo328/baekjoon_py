'''
N,M=map(int,input().split())
a=[];b=[];c=[]
for i in range(N):
    a.append(input())
for i in range(M):
    b.append(input())
for i in b:
    if i in a:
        c.append(i)
print(len(c))
print(*c,sep='\n')

#sys.stdin.readline()
'''
N,M=map(int,input().split())
a=set()
b=set()

for i in range(N):
    a.add(input())
for i in range(M):
    B=input()
    b.add(input())
c=sorted(list(a & b))
print(len(c))
for i in c:
    print(c)