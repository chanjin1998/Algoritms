from collections import deque
import sys

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


m, n = map(int, sys.stdin.readline().split())
graph = []
visited = [[0 for j in range(m)] for i in range(n)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()
max_cnt = 0
for i in range(len(graph)):
    if 0 in graph[i]:
        print(-1)
        exit()
    else:
        max_num = max(graph[i])
        if max_num > max_cnt:
            max_cnt = max_num
print(max_cnt - 1)