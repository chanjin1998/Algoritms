from collections import deque
import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))
w_max = 0
for line in graph:
  for val in line:
    w_max = max(val,w_max)

def bfs(j,k,i):
  
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  q = deque()
  q.append((j,k))
  while q:
    x,y = q.popleft()
    visited[x][y] = 1
    for a in range(4):
      nx = x + dx[a]
      ny = y + dy[a]
      if nx<0 or nx >=n or ny<0 or ny>=n:
        continue
      if visited[nx][ny] == 0 and graph[nx][ny] > i:
        visited[nx][ny] = 1
        q.append((nx,ny))

res = []
for i in range(w_max):
  
  visited = [[0]*n for _ in range(n)]
  cnt = 0
  for j in range(n):
    for k in range(n):

      if graph[j][k] > i and visited[j][k] == 0:
        bfs(j,k,i)
        cnt += 1
  res.append(cnt)
print(max(res))