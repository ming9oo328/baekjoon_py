roll_num = int(input())
p_num = int(input())
expect_max = 0
real_max = 0
roll = [0 for i in range(roll_num)]
for i in range(1,p_num+1):
    s_idx,e_idx=map(int,input().split(" "))
    if (e_idx-s_idx)>expect_max:
        expect_max = e_idx-s_idx
        expect_maxP = i    
    s_idx-=1
    e_idx-=1
    for j in range(s_idx,e_idx+1):
        if (roll[j]==0):
            roll[j] = i
for i in range(1,p_num+1):
    cnt = 0
    for j in range(roll_num):
        if i==roll[j]:
            cnt+=1
    if cnt>real_max:
        real_max = cnt
        real_maxP = i
print(expect_maxP)
print(real_maxP)