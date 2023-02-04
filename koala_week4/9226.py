moeum = ['a','e','i','o','u']
while True:
    word = input()
    newword = []
    if word == "#":
        break
    word = list(word)
    for i in range(len(word)):
        if word[i] in moeum:
            tmp = 0
            for j in range(i,len(word)):
                newword.insert(tmp,word[j])
                tmp+=1
            newword.append("ay")
        else:
            newword.append(word[i])
    for i in range(len(newword)):
        print(newword[i],end ='')