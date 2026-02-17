# 숫자 빠르게 찾기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# anwser = []
# for _ in range(m):
#     anwser.append(int(input()))

anwser = [int(input()) for _ in range(m)]

for i in anwser:
    if i in arr:
        print(arr.index(i)+1)
    else:
        print(-1)