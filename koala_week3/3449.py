T = int(input())
for i in range(T):
    cnt = 0
    num1 = list(input())
    num2 = list(input())
    for j in range(len(num1)):
        if (num1[j] != num2[j]):
            cnt+=1
    print("Hamming distance is "+str(cnt)+".")