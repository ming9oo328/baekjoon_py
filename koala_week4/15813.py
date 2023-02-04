N = int(input())
sum=0
name = str(input())
for i in range(N):
    sum+=int(ord(name[i]))
sum-=64*N
print(sum)