import sys
input = sys.stdin.read

print(sum(map(int,input().replace('\n','').split(','))))