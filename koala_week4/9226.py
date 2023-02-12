'''
moeum = ['a','e','i','o','u']
while True:
    word = input()
    newword = []
    stop = 0
    if word == "#":
        break
    for i in range(len(word)):
        while (word[i] in moeum) == False:
            newword.append(word[i])
            stop += i
    tmp = 0
    print(*newword)
    for j in range(stop,len(word)):
        newword.insert(tmp,word[j])
        tmp+=1
    newword.append("ay")

    for i in range(len(newword)):
        print(newword[i],end ='')
    print()
'''

moeum = ['a','e','i','o','u']
while True:
    word = list(input())
    if word[0] == "#":
        break
    for i in range(len(word)):
        if word[0] in moeum:
            break
        else:
            word+=word[0]
            del word[0]
    word+="ay"
    for i in range(len(word)):
        print(word[i],end ='')
    print()