import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

q = deque(range(1, N + 1))
ans = []

while q:
    # (K-1)번 회전: 앞을 빼서 뒤에 붙이기
    for _ in range(K - 1):
        q.append(q.popleft())
        # print(f"q: {q}")
    
    # 이제 맨 앞이 K번째 사람
    ans.append(q.popleft())
    # print(f'ans: {ans}')

print(*ans)