import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
value = list(map(int,sys.stdin.readline().split()))
q = deque()
node = 0
cnt = 0
for i in range(1,n+1):
  q.append(i)
while node < m:
  if q[0] == value[node]:
    q.popleft()
    node += 1
  else:
    mid = int(len(q) / 2)
    if q.index(value[node]) > mid:
      tmp = q.pop()
      q.appendleft(tmp)
      cnt += 1
    else:
      tmp = q.popleft()
      q.append(tmp)
      cnt += 1
print(cnt)