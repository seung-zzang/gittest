import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def print_nm(n, m):
    for _ in range(n):
        print('1' * m)


print_nm(n,m)