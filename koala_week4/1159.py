N = int(input())
dict = {}
plist = []
cnt = 0
for i in range(N):
    p = list(input())
    if p[0] in dict.keys():
        dict[p[0]]+=1
    else:
        dict[p[0]]=1
        
for key,value in dict.items():
    if value>=5:
        plist.append(key)
        cnt+=1

if cnt==0:
    print("PREDAJA")
else:
    plist = sorted(plist)
    for i in range(len(plist)):
        print(plist[i],end = "")