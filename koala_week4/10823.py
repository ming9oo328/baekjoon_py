s=""
while True :
    try:
        s+=input()
    except EOFError:
        break
print(sum(map(int,s.split(','))))