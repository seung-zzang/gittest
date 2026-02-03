import sys
input = sys.stdin.readline

str = list(input().strip())

match_dict = {
    ")":"(",
    "}":"{",
    "]":"["
}

cnt = 0

while str:
    if str.pop() in match_dict:
        cnt += 1
    else:
        cnt -= 1

if cnt == 0:
    print('Yes')

else:
    print('No')


