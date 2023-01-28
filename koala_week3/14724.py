N = int(input())
maxnum=[]
club = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]
for i in range(9):
        score = list(map(int,input().split(" ")))
        maxnum.append(max(score))
maxindex = maxnum.index(max(maxnum))
print(club[maxindex])