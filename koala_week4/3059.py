alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
T = int(input())
for i in range(T):
    sum = 0
    s = set(input())
    cha = alphabet-s
    for j in cha:
        sum+=ord(j)
    print(sum)