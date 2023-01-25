import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    S = sum(map(int,input().split(" ")))
    print(S)
