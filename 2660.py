from collections import deque
import sys

n = int(sys.stdin.readline())
l = int(sys.stdin.readline())

graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
for i in range(l):
  a,b = map(int,sys.stdin.readline().split())
  graph[a] += [b]
  graph[b] += [a]
  
visited[1] = 1
q = deque()
q.append(1)
while q:
  alpha = q.popleft()
  for nx in graph[alpha]:
    if visited[nx] == 0:
      q.append(nx)
      visited[nx] = 1
print(sum(visited)-1)