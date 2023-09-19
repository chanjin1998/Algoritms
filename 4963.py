from collections import deque
import sys

def bfs(a,b):
  q = deque()
  q.append((a,b))

  dx = [-1,1,0,0,1,-1,1,-1]
  dy = [0,0,-1,1,1,-1,-1,1]

  while q:
    x,y = q.popleft()
    visited[x][y] = 1

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0>nx or nx >=h or 0>ny or ny>=w:
        continue

      if graph[nx][ny] == 1 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        q.append((nx,ny))

while True:
  w,h = map(int,sys.stdin.readline().split())

  if w==0 and h ==0:
    break

  graph = []
  for k in range(h):
    graph.append(list(map(int,sys.stdin.readline().split())))
  cnt  = 0
  visited = [ [ 0 for _ in range(w)] for _ in range(h)]

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1 and visited[i][j] ==0:
        bfs(i,j)
        cnt += 1

  print(cnt)
