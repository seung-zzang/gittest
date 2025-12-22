n = int(input())

def func(n):
    (n % 2 == 0) and ((n // 10 + n % 10) % 5 == 0)
    return n


if func(n):
    print("Yes")

else:
    print("No")