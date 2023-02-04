for i in range(3):
    s = str(input())
    cnt = 1
    max_cnt = []
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            cnt+=1
        else:
            max_cnt.append(cnt)
            cnt = 1
    max_cnt.append(cnt)
    print(max(max_cnt))

