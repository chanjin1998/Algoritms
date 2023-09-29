import sys
from collections import deque
n = int(sys.stdin.readline())
visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs():
  if a== b:
    pass

  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0:
        visited[i][j] == 1
        dfs()
def checkUp(i,j):
  q = deque()
  q.append((i,j))
  dx = [-1,1]
  dy = [0,0]
  while q:
    x,y = q.popleft()
    visited[x][y] = 1
    for i in range(2):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n:
        if visited[nx][ny] ==0:
          visited[nx][ny] = 1
          q.append((nx,ny))
