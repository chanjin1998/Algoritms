import sys
from collections import deque
m,n,h = map(int,sys.stdin.readline().split())
graph = []
visited = [0]
for _ in range(h):
  tmp_graph = []
  for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    tmp_graph.append(tmp)
  graph.append(tmp_graph)
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1:
        q.append((i,j,k))
while q:
  z,y,x = q.popleft()
  dz = [1,-1,0,0,0,0]
  dy = [0,0,1,-1,0,0]
  dx = [0,0,0,0,1,-1]

  for i in range(6):
    nz = z + dz[i]
    ny = y + dy[i]
    nx = x + dx[i]

    if nz>=0 and nz<h and ny>=0 and ny<n and nx>=0 and nx<m:
      if visited[nz][ny][nx] == 0 and graph[nz][ny][nx] == 0:
        q.append((nz,ny,nx))
        visited[nz][ny][nx] = visited[z][y][x] + 1
check = 0
max_val = 0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if visited[i][j][k] == 0 and graph[i][j][k] == 0:
        check = -1
      elif visited[i][j][k]> max_val:
        max_val = visited[i][j][k]
if check == 0:
  print(max_val)
else:
  print(-1)