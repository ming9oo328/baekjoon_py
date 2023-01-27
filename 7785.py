n = int(input())
dict = {}
for i in range(n):
    name,log = input().split(" ")
    if log == "leave":
        del(dict[name])
    else:
        dict[name]=log
dict = sorted(dict.keys(), reverse = True)
for key in dict:
    print(key)