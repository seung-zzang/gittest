import sys
input = sys.stdin.readline

n = int(input())

def square(n):
    for i in range(1, n**2+1):
        print((i-1) % 9 +1, end =' ')
        if i % n == 0:
            print()

square(n)