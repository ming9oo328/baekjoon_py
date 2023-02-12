N = int(input())
info = [[] for row in range(N)]
for i in range(N):
    age, name = input().split(' ')
    info[i].append(int(age))
    info[i].append(name)

info.sort(key = lambda x:x[0])

for i in range(N):
    for j in range(2):
        print(info[i][j],end = " ")
    print()  