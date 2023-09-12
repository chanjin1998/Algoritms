from collections import deque
import sys

n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
bfs_list = []
dfs_list = []

visited = [0] * (n+1)
visited_dfs = [0] * (n+1)

def bfs(v):
  q = deque()
  q.append(v)
  visited[v] = 1
  bfs_list.append(v)
  while q:
    alpha = q.popleft()
    for nx in graph[alpha]:
      if visited[nx] == 0:
        q.append(nx)
        visited[nx] = 1
        bfs_list.append(nx)


def dfs(v):
  visited_dfs[v] = 1
  dfs_list.append(v)
  for nx in graph[v]:
    if visited_dfs[nx] == 0:
      dfs(nx)

for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[a] += [b]
  graph[b] += [a]
  graph[a].sort()
  graph[b].sort()

dfs(v)
print(*dfs_list)
bfs(v)
print(*bfs_list)