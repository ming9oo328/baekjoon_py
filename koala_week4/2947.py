namu = list(map(int,input().split(" ")))
answer = [1,2,3,4,5]
while (namu != answer):
    for i in range(len(namu)-1):
        if namu[i]>namu[i+1]:
            tmp = namu[i]
            namu[i]=namu[i+1]
            namu[i+1]=tmp
            print(*namu, end =" ")
            print()
