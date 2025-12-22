import sys
input = sys.stdin.readline

n = int(input())

result = 0 

def func(n):
    for i in range(1, n+1):
        result += i
    return result // 10

print(func(n))
