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
day = 0
for row in graph:
    for i in row:
        if i == 0:  # 익지 않은 토마토가 있으면(=토마토가 모두 익지 못하는 상황) -1 출력
            print(-1)
            exit() # 다음 행의 여부와 관계 없이 -1만 출력해야하므로 종료시킴
    else: # 그래프에서 가장 큰 값이 마지막으로 익은 토마토임 → 한 줄씩 최댓값을 day로 갱신하며 최댓값 찾기
        day = max(day, max(row)) 

# 처음 시작을 0이 아닌 1부터 했으므로 -1을 해야 날짜를 구할 수 있음 
print(day-1)
