import sys
input = sys.stdin.readline

n = int(input())


def func(n):

    result = 0 
    
    for i in range(1, n+1):
        result += i
    return result // 10

print(func(n))
