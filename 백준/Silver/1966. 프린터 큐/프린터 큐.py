import sys
from collections import deque
T = int(sys.stdin.readline())

for _ in range(T):
  cnt = 1
  n, p = map(int,sys.stdin.readline().split())
  q = deque(map(int,sys.stdin.readline().split()))

  while q:
    if p == 0:
      if q[p] < max(q):
        q.append(q.popleft())
        p = len(q) - 1
      else:
        print(cnt)
        break
    else:
      if q[0] < max(q):
        q.append(q.popleft())
        p -= 1
      else:
        q.popleft()
        p -= 1
        cnt += 1