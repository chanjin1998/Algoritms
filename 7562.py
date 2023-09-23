from collections import deque
import sys

num = int(sys.stdin.readline())

def bfs():
  q = deque()
  q.append((a,b))
  dx = [-2,-2,-1,-1,1,1,2,2]
  dy = [-1,1,-2,2,-2,2,-1,1]
  
  while q:
    x,y = q.popleft()
    if x==t_a and y ==t_b:
      return visited[x][y]-1
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<= nx < n and 0<=ny<n:
        if visited[nx][ny] == 0:
          visited[nx][ny] = visited[x][y]+1
          q.append((nx,ny))

for i in range(num):
  n = int(sys.stdin.readline())
  a,b = map(int,sys.stdin.readline().split())
  t_a,t_b = map(int,sys.stdin.readline().split())
  visited = [[0 for _ in range(n)] for _ in range(n)]
  visited[a][b] = 1
  print(bfs())

