while True:
    a=input()
    b=""
    if a=="END":
        break
    else:
        for i in range(len(a)-1,-1,-1):
            b+=a[i]
        print(b)