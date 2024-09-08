import sys
import heapq
m,n,k = map(int,sys.stdin.readline().split()) #m은 높이 n은 너비
# 1,1 - 2,5
# 1,1 1,2 1,3 1,4

# 0,2 4,4
# 0,2 0,3
# 1,2 1,3
# 2,2 2,3
# 3,2 3,3
graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
res = []
count = 0
for _ in range(k):
  a,b,c,d = map(int,sys.stdin.readline().split())
  for i in range(b,d):
    for j in range(a,c):
      graph[i][j] = 1

def bfs(start,end):
  q = []
  cnt = 1
  heapq.heappush(q,(start,end))
  visited[start][end] = 1
  graph[start][end] = 2
  while q:
    y,x = heapq.heappop(q)
    # print(y,x)
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0<= ny <m and 0<= nx <n:
        if graph[ny][nx] == 0:
          visited[ny][nx] = 1
          graph[ny][nx] = 2
          heapq.heappush(q,(ny,nx))
          cnt += 1
  # print(graph)
  # print(cnt)
  return cnt
for i in range(m):
  for j in range(n):
    if graph[i][j] == 0:
      res.append(bfs(i,j))
      count += 1
res.sort()
print(count)
print(*res)