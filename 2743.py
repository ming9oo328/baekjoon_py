import sys
input = sys.stdin.readline

a=list(input())
del a[-1]
print(len(a))