from collections import deque
from email import charset
import sys

n = int(sys.stdin.readline())
graph = []
lines= []
for _ in range(n):
  lines.append(list(map(str,sys.stdin.readline().strip())))
graph = [list(line) for line in lines] 
visited = [[0 for _ in range(n)] for _ in range(n)]
visited1 = [[0 for _ in range(n)] for _ in range(n)]

nor_cnt = 0
abnor_cnt = 0

def bfs(i,j):
  q = deque()
  q.append((i,j))
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while q:
    x,y = q.popleft()
    visited[x][y] = 1
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0<= nx <n and 0<=ny <n:
        if graph[nx][ny] == 'R' and visited[nx][ny]==0:
          visited[nx][ny] = 1
          q.append((nx,ny))

def blue_bfs(i,j):
  q = deque()
  q.append((i,j))
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while q:
    x,y = q.popleft()
    visited[x][y] = 1
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0<= nx <n and 0<=ny <n:
        if graph[nx][ny] == 'B' and visited[nx][ny]==0:
          visited[nx][ny] = 1
          q.append((nx,ny))

def green_bfs(i,j):
  q = deque()
  q.append((i,j))
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while q:
    x,y = q.popleft()
    visited[x][y] = 1
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0<= nx <n and 0<=ny <n:
        if graph[nx][ny] == 'G' and visited[nx][ny]==0:
          visited[nx][ny] = 1
          q.append((nx,ny))

def red_green_bfs(i,j):
  q = deque()
  q.append((i,j))
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while q:
    x,y = q.popleft()
    visited1[x][y] = 1
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0<= nx <n and 0<=ny <n:
        if (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') and visited1[nx][ny]==0:
          visited1[nx][ny] = 1
          q.append((nx,ny))

def blue1_bfs(i,j):
  q = deque()
  q.append((i,j))
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while q:
    x,y = q.popleft()
    visited1[x][y] = 1
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0<= nx <n and 0<=ny <n:
        if (graph[nx][ny] == 'B') and visited1[nx][ny]==0:
          visited1[nx][ny] = 1
          q.append((nx,ny))

for i in range(n):
  for j in range(n):
    if graph[i][j] == 'R' and visited[i][j] ==0:
      bfs(i,j)
      nor_cnt += 1
    elif graph[i][j] == 'B' and visited[i][j] ==0:
      blue_bfs(i,j)
      nor_cnt +=1
    elif graph[i][j] == 'G' and visited[i][j] ==0:
      green_bfs(i,j)
      nor_cnt +=1

for i in range(n):
  for j in range(n):
    if (graph[i][j] == 'R' or graph[i][j] == 'G') and visited1[i][j] ==0:
      red_green_bfs(i,j)
      abnor_cnt += 1
    elif graph[i][j] == 'B' and visited1[i][j] ==0:
      blue1_bfs(i,j)
      abnor_cnt +=1   
print(nor_cnt,abnor_cnt)
