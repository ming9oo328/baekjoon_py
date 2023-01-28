
char = list(input())
cnt = 1
for i in range(len(char)):
    if char[i]==" ":
        cnt+=1
if char[0] == " ":
    cnt-=1
if char[-1] == " ":
    cnt-=1
print(cnt)