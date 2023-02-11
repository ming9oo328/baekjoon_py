N = int(input())
for i in range(N):
    distance = []
    x,y = input().split(" ")
    for j in range(len(x)):
        if ord(x[j])<=ord(y[j]):
           distance.append(ord(y[j]) - ord(x[j]))
        else:
           distance.append((ord(y[j])+26) - ord(x[j]))
    print("Distances:", *distance) 