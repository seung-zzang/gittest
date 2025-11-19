h, m = map(int, input().split(':'))
h = (h+1 % 24) 
print(f'{h}:{m}')