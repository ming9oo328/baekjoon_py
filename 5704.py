import sys
input = sys.stdin.readline
#본 문제에서는 위 코드를 사용하면 출력초과가 발생한다.

while True:
    sentence = input()
    is_p = "Y"
    if sentence == "*":
        break
    else:
        for c in range(97,123):
            if sentence.find(chr(c)) == -1:
                is_p = "N"
                break
        print(is_p)    