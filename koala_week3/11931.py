import sys
input = sys.stdin.readline

N=int(input())
list = []
for i in range(N):
    list.append(int(input()))

list = sorted(list,reverse=True)
for i in range(len(list)): 
    print(list[i])