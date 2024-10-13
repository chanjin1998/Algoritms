import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
answer = [-1 for _ in range(N)]
stack = []
for i in range(N):
  while stack and A[i] > stack[-1][1]:
    index, value = stack.pop()
    answer[index] = A[i]

  stack.append((i,A[i]))
print(*answer)