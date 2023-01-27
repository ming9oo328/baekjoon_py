a = list(input())
JOI = 0
IOI = 0
for i in range(len(a)-2):
    if a[i] == 'J':
        if a[i+1] == 'O' and a[i+2] == 'I':
            JOI+=1
    if a[i] == 'I':
        if a[i+1] == 'O' and a[i+2] == 'I':
            IOI+=1
print(JOI)
print(IOI)