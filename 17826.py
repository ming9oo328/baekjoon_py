import sys
input = sys.stdin.readline

score = list(map(int,input().split(" ")))
hongik = int(input())

rank = score.index(hongik)+1

if 1<=rank and rank<=5:
    print("A+")
elif rank<=15:
    print("A0")
elif rank<=30:
    print("B+")
elif rank<=35:
    print("B0")
elif rank<=45:
    print("C+")
elif rank<=48:
    print("C0")
else:
    print("F")