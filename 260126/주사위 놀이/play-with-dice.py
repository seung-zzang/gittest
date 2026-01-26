import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

answer = [0] * 7

for i in arr:
    answer[i] = answer[i] + 1

for j in range(1,7):
    print(f"{j} - {answer[j]}")
