# import sys
# from collections import deque

# n,m,t = map(int,sys.stdin.readline().split())
# graph = []
# for _ in range(n):
#   graph.append(list(map(int,sys.stdin.readline().split())))
# origin_visited = [[0 for _ in range(m)] for _ in range(n)]
# fast_visited = [[0 for _ in range(m)] for _ in range(n)]

# def origin_bfs(y,x):
#   q = deque()
#   q.append((y,x))
#   origin_visited[y][x] = 1
#   while q:
#     y,x = q.popleft()
#     dy = [1,-1,0,0]
#     dx = [0,0,1,-1]

#     for i in range(4):
#       ny = y + dy[i]
#       nx = x + dx[i]

#       if ny>=0 and ny<n and nx>=0 and nx<m:
#         if origin_visited[ny][nx] == 0 and graph[ny][nx] == 0:
#           q.append((ny,nx))
#           origin_visited[ny][nx] = origin_visited[y][x] + 1

# def fast_bfs(y,x):
#   q = deque()
#   q.append((y,x))
#   fast_visited[y][x] = 1
#   while q:
#     y,x = q.popleft()
#     dy = [1,-1,0,0]
#     dx = [0,0,1,-1]

#     for i in range(4):
#       ny = y + dy[i]
#       nx = x + dx[i]

#       if ny>=0 and ny<n and nx>=0 and nx<m:
#         if fast_visited[ny][nx] == 0 and graph[ny][nx] == 0:
#           q.append((ny,nx))
#           fast_visited[ny][nx] = fast_visited[y][x] + 1
#         elif fast_visited[ny][nx] == 0 and graph[ny][nx] == 2:
#           fast_visited[ny][nx] = fast_visited[y][x] + 1
#           fast_visited[n-1][m-1] = fast_visited[y][x] + (n-1-y) + (m-1-x)
#           break
# origin_bfs(0,0)
# fast_bfs(0,0)
# origin_val = origin_visited[n-1][m-1] -1
# fast_val = fast_visited[n-1][m-1] -1

# # if min(origin_val,fast_val)>t:
# #   print("Fail")
# # elif origin_val == -1 and fast_val == -1:
# #   print("Fail")
# # elif origin_val == -1 and fast_val != -1:
# #   print(fast_val)
# # elif origin_val != -1 and fast_val == -1:
# #   print(origin_val)
# # else:
# #   print(min(origin_val,fast_val))
# if min(origin_val,fast_val) != -1:
#   print(min(origin_val,fast_val))
# elif origin_val == -1 and fast_val == -1:
#   print("Fail")
# elif min(origin_val,fast_val)>t:
#   print("Fail")

import sys
from collections import deque
input = sys.stdin.readline
N, M, T = map(int,input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m = [list(map(int,input().split())) for _ in range(N)]
q = deque()
visited = [[0] * M for _ in range(N)]
 
def bfs():
    gram = 10001
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        # 공주님이 있는 곳에 도착했을 때
        if (x, y) == (N-1, M-1):
            return min(visited[x][y]-1, gram)
        # 그람이 있는 곳에 도착했을 때
        if m[x][y] == 2:
            gram = visited[x][y]-1 + N-1-x + M-1-y
 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if m[nx][ny] == 0 or m[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return gram
 
res = bfs()
if res > T:
    print('Fail')
else:
    print(res)
