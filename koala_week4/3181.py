s = input().split(" ")
jullim = ""
delWord = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
for i in range(len(s)):
    word = ""
    word+=s[i]
    if s[i] in delWord:
        if i!=0:
            continue
    jullim+=word[0].upper()
print(jullim)