from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

def bfs(x,y):

  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  q = deque()
  q.append((x,y))
  graph[x][y] = 0
  global cnt
  while q:
    x,y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        q.append((nx,ny))
        cnt += 1

res = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      cnt = 1
      bfs(i,j)
      res.append(cnt)
# print(graph)
print(len(res))
print(max(res))