N = int(input())
book = []
list=[]
cnt = 0
max_cnt = 0
max_book = ""

for i in range(N):
    book.append(input())
for i in range(len(book)):
    for j in range(len(book)):
        if book[i] == book[j]:
            cnt+=1
    if cnt>max_cnt:
        max_cnt = cnt
        max_book = book[i]
    if cnt == max_cnt and max_book!=book[i]:
        list.append(max_book)
        list.append(book[i])
        list.sort()
        max_book = list[0]
    cnt = 0
print(max_book)