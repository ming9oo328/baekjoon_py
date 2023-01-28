import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dict = {}
for i in range(N):
    address, password = input().split()
    dict[address] = password
for i in range(M):
    print(dict[input().strip()])