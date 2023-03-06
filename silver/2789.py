delLetter = ["C","A","M","B","R","I","D","G","E"]
word = list(input())
for i in range(len(word)):
    if word[i] in delLetter:
        word[i] = '*'
for i in range(len(word)):
    if word[i] != '*':
        print(word[i],end = '')