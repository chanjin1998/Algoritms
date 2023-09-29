from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[a] += [b]
  graph[b] += [a]

res = []
cnt = 0
for i in range(1,n+1):
  if visited[i] == 0:
    visited[i] = 1
    cnt += 1
    q = deque()
    q.append(i)
    while q:
      alpha = q.popleft()
      for nx in graph[alpha]:
        if visited[nx] == 0:
          q.append(nx)
          # res.append(i)
          visited[nx] = 1
  else:
    continue
print(cnt)