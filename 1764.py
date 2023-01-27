N,M = map(int,input().split())
nohear = set()
nosee = set()
for i in range(N):
    nohear.add(input())
for i in range(M):
    nosee.add(input())
same = sorted(list(nohear & nosee))
print(len(same))
for i in same:
    print(i)