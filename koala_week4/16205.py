case,word = input().split(" ")
if case =="1":
    camel = word
    list = list(word)
    for i in range(len(list)):
        if list[i].isupper() is True:
            list.insert(i,'_')
            
    print(camel)
    for i in range(len(list)):
        print(list[i],end = '')
    print()
    print(word)