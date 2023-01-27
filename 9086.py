#import sys
#input = sys.stdin.readline

T=int(input())
for i in range(T):
    char = list(input())
    print(char[0]+char[-1])