N, K = map(int,input().split(" "))
newgugu = []
for i in range(1,K+1):
    newgugu.append(int(str(N*i)[::-1]))
    
print(max(newgugu))
