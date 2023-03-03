N = int(input())
gWord = 0
for i in range(N):
    word = list(input())
    check = []
    count = 0
    
    #경우1 : 겹치는 글자가 없는 경우
    for letter in word:
        if letter not in check:
            check.append(letter)
    if word == check:
        gWord +=1
    
    #경우2: 겹치는 글자가 있는 경우
    elif word != check:
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
               count+=1 
        if count == len(check)-1:
            gWord +=1
            
print(gWord)